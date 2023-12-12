from joinPath import join_path

def list_directory(self, path=""):
    target_path = join_path(self.current_directory, path)
    if target_path in self.file_system and isinstance(self.file_system[target_path], dict):
        return list(self.file_system[target_path].keys())
    else:
        return None



