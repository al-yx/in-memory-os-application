from joinPath import join_path
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