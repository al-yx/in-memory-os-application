from joinPath import join_path
def move(self, source, destination):
    source_path = join_path(self.current_directory, source)
    destination_path = join_path(self.current_directory, destination)

    if source_path in self.file_system:
        self.file_system[destination_path] = { **self.file_system.pop(source_path), **self.file_system[destination_path]}
    elif source in self.file_system[self.current_directory]:
        if destination_path in self.file_system:
            file_to_move = { source : self.file_system[self.current_directory][source] }
            del self.file_system[self.current_directory][source]
            self.file_system[destination_path] = { **self.file_system[destination_path], **file_to_move}
        else:
            print(f"Error: Destination not found - {destination_path}")
    else:
        print(f"Error: Source not found - {source}")