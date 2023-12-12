from inMemoryFile import InMemoryFileSystem

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
