from joinPath import join_path
def copy(self, source, destination):
    source_path = join_path(self.current_directory, source)
    destination_path = join_path(self.current_directory, destination)

    if source_path in self.file_system:
        self.file_system[destination_path] = {**self.file_system[source_path].copy(), **self.file_system[destination_path]}
    elif source in self.file_system[self.current_directory]:
        if destination_path in self.file_system:
            file_to_copy = { source : self.file_system[self.current_directory][source] }
            self.file_system[destination_path] = { **self.file_system[destination_path], **file_to_copy}
        else:
            print(f"Error: Destination not found - {destination_path}")
    else:
        print(f"Error: Source not found - {source}")