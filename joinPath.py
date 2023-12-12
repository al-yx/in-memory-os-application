
import os
import re

def join_path(current_directory, path):
    if path == "": return current_directory
    if current_directory == "/": return current_directory + path
    return current_directory + '/' + path
