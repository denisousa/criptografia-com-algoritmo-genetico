import os
from project import app
from zipfile import ZipFile
import shutil


def get_all_file_paths(directory): 
    file_paths = [] 

    for root, directories, files in os.walk(directory): 
        for filename in files: 
            # join the two strings in order to form the full filepath. 
            filepath = os.path.join(root, filename) 
            file_paths.append(filepath)

    return file_paths 
