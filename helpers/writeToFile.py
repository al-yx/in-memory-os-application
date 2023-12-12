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