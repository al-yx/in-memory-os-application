
from joinPath import join_path
def create_directory(self, directory_name):
    path = join_path(self.current_directory, directory_name)
    self.file_system[path] = {}
    self.file_system[self.current_directory][directory_name] = ""
