import os
import re

class InMemoryFileSystem:
    def __init__(self):
        self.current_directory = "/"
        self.file_system = {
            "/": {}
        }

    def change_directory(self, path):
        if path == "/":
            self.current_directory = "/"
        elif path == "..":
            # Move to the parent directory
            if self.current_directory != "/":
                self.current_directory = os.path.dirname(self.current_directory)
        elif path.startswith("/"):
            # Absolute path
            if path in self.file_system:
                self.current_directory = path
            else:
                print("Path not found")
        else:
            # Relative path
            target_path = join_path(self.current_directory, path)
            if target_path in self.file_system:
                self.current_directory = target_path
            else:
                print("Path not found")

    def list_directory(self, path="."):
        print(self.file_system)
        target_path = join_path(self.current_directory, path)
        if target_path in self.file_system and isinstance(self.file_system[target_path], dict):
            return list(self.file_system[target_path].keys())
        else:
            return None

    def create_directory(self, directory_name):
        path = join_path(self.current_directory, directory_name)
        self.file_system[path] = {}
        self.file_system[self.current_directory][directory_name] = ""

    def create_file(self, file_name):
        self.file_system[self.current_directory][file_name] = ""

    def read_file(self, file_name):
        if file_name.startswith("/"):
            index = file_name.rindex('/')
            file_path = file_name[:index]
            if file_path in self.file_system:
                new_file_name = file_name[index:]
                return self.file_system[file_path].get(new_file_name, None)
            # else:
            #     print("Directory does not exist")
        return self.file_system[self.current_directory].get(file_name, None)

    def write_to_file(self, file_name, content):
        if file_name.startswith("/"):
            index = file_name.rindex('/')
            file_path = file_name[:index]
            if file_path in self.file_system:
                new_file_name = file_name[index:]
                self.file_system[file_path][new_file_name] = content
            else:
                print("Directory does not exist")

        else:
            self.file_system[self.current_directory][file_name] = content

    def move(self, source, destination):
        source_path = join_path(self.current_directory, source)
        destination_path = join_path(self.current_directory, destination)

        if source_path in self.file_system:
            self.file_system[destination_path] = { **self.file_system.pop(source_path), **self.file_system[destination_path]}
        elif source in self.file_system[self.current_directory]:
            if destination_path in self.file_system:
                file_to_move = { source : self.file_system[self.current_directory][source] }
                del self.file_system[self.current_directory][source]
                self.file_system[destination_path] = { **self.file_system[destination_path], **file_to_move}
            else:
                print(f"Error: Destination not found - {destination_path}")
        else:
            print(f"Error: Source not found - {source}")

    def copy(self, source, destination):
        source_path = join_path(self.current_directory, source)
        destination_path = join_path(self.current_directory, destination)

        if source_path in self.file_system:
            self.file_system[destination_path] = {**self.file_system[source_path].copy(), **self.file_system[destination_path]}
        elif source in self.file_system[self.current_directory]:
            if destination_path in self.file_system:
                file_to_copy = { source : self.file_system[self.current_directory][source] }
                self.file_system[destination_path] = { **self.file_system[destination_path], **file_to_copy}
            else:
                print(f"Error: Destination not found - {destination_path}")
        else:
            print(f"Error: Source not found - {source}")

    def remove(self, path):
        if path.startswith("/"):
            index = path.rindex('/')
            print(index)
            file_path = path[:index]
            print(file_path)
            if file_path in self.file_system:
                file_name = path[index+1:]
                print(file_name)
                del self.file_system[file_path][file_name]
                try:
                    del self.file_system[path]
                finally:
                    return
            else:
                print("Directory does not exist")
        else:
            target_path = join_path(self.current_directory, path)
            if target_path in self.file_system:
                del self.file_system[target_path]
                del self.file_system[self.current_directory][path]
            elif path in self.file_system[self.current_directory]:
                del self.file_system[self.current_directory][path]
            else:
                print(f"Error: File or directory not found - {path}")

    def grep(self, pattern, file_name):
        content = self.read_file(file_name)
        if content is not None:
            matches = re.findall(pattern, content)
            return matches
        else:
            print(f"Error: File not found - {file_name}")

def print_prompt(current_directory):
    print(f"{current_directory}$ ", end="")

def join_path(current_directory, path):
    if path == "": return current_directory
    if current_directory == "/": return current_directory + path
    return current_directory + '/' + path

def main():
    file_system = InMemoryFileSystem()

    while True:
        print_prompt(file_system.current_directory)
        user_input = input().strip()

        if user_input == "exit":
            break

        command, *args = user_input.split()

        if command == "cd":
            if args:
                file_system.change_directory(args[0])
            else:
                print("Usage: cd <directory>")
        elif command == "ls":
            path = args[0] if args else ""
            contents = file_system.list_directory(path)
            if contents is not None:
                print("\n".join(contents))
            else:
                print(f"Error: Directory not found - {path}")
        elif command == "mkdir":
            if args:
                file_system.create_directory(args[0])
            else:
                print("Usage: mkdir <directory>")
        elif command == "touch":
            if args:
                file_system.create_file(args[0])
            else:
                print("Usage: touch <file>")
        elif command == "cat":
            if args:
                content = file_system.read_file(args[0])
                if content is not None:
                    print(content)
                else:
                    print(f"Error: File not found - {args[0]}")
            else:
                print("Usage: cat <file>")
        elif command == "echo":
            print(args)
            if len(args) >= 2 and args[1] == ">":
                file_name = args[0]
                content = " ".join(args[2:])
                file_system.write_to_file(file_name, content)
            else:
                print("Usage: echo file > 'text'")
        elif command == "mv":
            if len(args) == 2:
                file_system.move(args[0], args[1])
            else:
                print("Usage: mv <source> <destination>")
        elif command == "cp":
            if len(args) == 2:
                file_system.copy(args[0], args[1])
            else:
                print("Usage: cp <source> <destination>")
        elif command == "rm":
            if args:
                file_system.remove(args[0])
            else:
                print("Usage: rm <file or directory>")
        elif command == "grep":
            if len(args) == 2:
                pattern = args[0]
                file_name = args[1]
                matches = file_system.grep(pattern, file_name)
                if matches:
                    print("\n".join(matches))
                else:
                    print(f"No matches found for pattern '{pattern}' in file '{file_name}'")
            else:
                print("Usage: grep <pattern> <file>")
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()
