# In-memory-os-application<br />
**Documentation for In-Memory File System**<br />
Implementation Overview:<br />
Main entry point of the system(**main.py**):<br />
An interactive shell to interact with the in-memory file system to support various functionalities commands:cd, ls, mkdir, touch, cat, echo, mv, cp, rm, grep, and exit.<br />

**InMemoryFileSystem class in InMemoryFile:**<br />
For easier debugging, testing, and modification of each function without affecting the entire codebase.<br />
**__init__(self)**: Initializes the in-memory file system to creates an instance of InMemoryFileSystem with the root directory (/) and an empty file system dictionary.<br />


**Imports used:**<br />
import os: Used for handling file paths. <br />
import rs: Used for regular expression matching in the grep method. <br />


# Helper Functions:<br />
**change_directory**: Handles changing the current directory based on the provided path.<br />
**list_directory**: Lists the contents of a directory.<br />
**create_directory**: Creates a new directory<br />
**create_file**: Creates a new file.<br />
**read_file**: Reads the content of a file.<br />
**write_to_file**: Writes content to a file.<br />
**move**: Moves a file or directory to a new location.<br />
**copy**: Copies a file or directory to a new location.<br />
**remove**: Removes a file or directory.<br />
**grep**: Searches for a pattern in a file.<br />

Utilities (joinPath.py):<br />
**join_path**: Combines the current directory and a given path to form a relevent path.<br />

# Data Structure:<br />
A dictionary to represent the file system. Each key is a directory path, and its corresponding value is another dictionary representing files and directories inside it.<br />

# To create an executable using PyInstaller for the in-memory file system <br />
Install Python and pip <br />
pip install pyinstaller <br />
#Create the Executable using PyInstaller <br />
pyinstaller --onefile main.py <br />
Run the generated executable: <br />
On Windows: <br />
main.exe <br />
