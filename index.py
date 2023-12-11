import os
import re

class InMemoryFileSystem:
    def __init__(self):
        self.current_directory = "/"
        self.file_system = {
            "/": {}
        }

    def change_directory(self, path):
        print(self.current_directory)
        print(self.file_system)
        print(path)
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
            target_path = os.path.join(self.current_directory, path)
            print(target_path)
            if target_path in self.file_system:
                self.current_directory = target_path
            else:
                print("Path not found")

    def list_directory(self, path="."):
        target_path = os.path.join(self.current_directory, path)
        # TODO: check if required
        target_path = target_path.replace("\\", '')
        if target_path in self.file_system and isinstance(self.file_system[target_path], dict):
            return list(self.file_system[target_path].keys())
        else:
            return None

    def create_directory(self, directory_name):
        path = os.path.join(self.current_directory, directory_name)
        print(path)
        self.file_system[path] = {}
        self.file_system[self.current_directory][directory_name] = ""

    def create_file(self, file_name):
        path = os.path.join(self.current_directory, file_name)
        self.file_system[self.current_directory][file_name] = ""

    def read_file(self, file_name):
        path = os.path.join(self.current_directory, file_name)
        return self.file_system[self.current_directory].get(file_name, None)

    def write_to_file(self, file_name, content):
        path = os.path.join(self.current_directory, file_name)
        self.file_system[self.current_directory][file_name] = content

    def move(self, source, destination):
        source_path = os.path.join(self.current_directory, source)
        destination_path = os.path.join(self.current_directory, destination)

        if source_path in self.file_system:
            self.file_system[destination_path] = self.file_system.pop(source_path)
        else:
            print(f"Error: Source not found - {source}")

    def copy(self, source, destination):
        source_path = os.path.join(self.current_directory, source)
        destination_path = os.path.join(self.current_directory, destination)

        if source_path in self.file_system:
            self.file_system[destination_path] = self.file_system[source_path].copy()
        else:
            print(f"Error: Source not found - {source}")

    def remove(self, path):
        target_path = os.path.join(self.current_directory, path)

        if target_path in self.file_system:
            del self.file_system[target_path]
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
            if len(args) >= 2 and args[1] == ">":
                file_name = args[-1]
                content = " ".join(args[2:-1])
                file_system.write_to_file(file_name, content)
            else:
                print("Usage: echo 'text' > file")
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
