import re

def grep(self, pattern, file_name):
    content = self.read_file(file_name)
    if content is not None:
        matches = re.findall(pattern, content)
        return matches
    else:
        print(f"Error: File not found - {file_name}")