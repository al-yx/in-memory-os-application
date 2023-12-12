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