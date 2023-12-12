import re
import helpers.changeDirectory  
import helpers.listDirectory
import helpers.createDirectory
import helpers.createFile
import helpers.readFile
import helpers.writeToFile
import helpers.move
import helpers.copy
import helpers.remove
import helpers.grep
class InMemoryFileSystem:
    def __init__(self):
        self.current_directory = "/"
        self.file_system = {
            "/": {}
        }

    def change_directory(self, path):
        helpers.changeDirectory.change_directory(self, path)

    def list_directory(self, path=""):
        return helpers.listDirectory.list_directory(self, path)

    def create_directory(self, directory_name):
        helpers.createDirectory.create_directory(self,directory_name)

    def create_file(self, file_name):
        helpers.createFile.create_file(self,file_name)

    def read_file(self, file_name):
        return helpers.readFile.read_file(self,file_name)

    def write_to_file(self, file_name, content):
        helpers.writeToFile.write_to_file(self, file_name, content)

    def move(self, source, destination):
        helpers.move.move(self, source, destination)

    def copy(self, source, destination):
        helpers.copy.copy(self, source, destination)

    def remove(self, path):
        helpers.remove.remove(self, path)

    def grep(self, pattern, file_name):
        return helpers.grep.grep(self, pattern, file_name)


