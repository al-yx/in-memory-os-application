import os
from joinPath import join_path

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