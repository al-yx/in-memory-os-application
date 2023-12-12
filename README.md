# In-memory-os-application
**Documentation for In-Memory File System**
Implementation Overview:
Main entry point of the system(**main.py**):
An interactive shell to interact with the in-memory file system to support various functionalities commands:cd, ls, mkdir, touch, cat, echo, mv, cp, rm, grep, and exit.

**InMemoryFileSystem class in InMemoryFile:**
For easier debugging, testing, and modification of each function without affecting the entire codebase.
**__init__(self)**: Initializes the in-memory file system to creates an instance of InMemoryFileSystem with the root directory (/) and an empty file system dictionary.


**Imports used:**
import os: Used for handling file paths
import rs: Used for regular expression matching in the grep method


# Helper Functions:
**change_directory**: Handles changing the current directory based on the provided path.
**list_directory**: Lists the contents of a directory.
**create_directory**: Creates a new directory.
**create_file**: Creates a new file.
**read_file**: Reads the content of a file.
**write_to_file**: Writes content to a file.
**move**: Moves a file or directory to a new location.
**copy**: Copies a file or directory to a new location.
**remove**: Removes a file or directory.
**grep**: Searches for a pattern in a file.

Utilities (joinPath.py):
**join_path**: Combines the current directory and a given path to form a relevent path.

# Data Structure:
A dictionary to represent the file system. Each key is a directory path, and its corresponding value is another dictionary representing files and directories inside it.

# To create an executable using PyInstaller for the in-memory file system 
Install Python and pip
pip install pyinstaller
#Create the Executable using PyInstaller
pyinstaller --onefile main.py
Run the generated executable:
On Windows:
main.exe
