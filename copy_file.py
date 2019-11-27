import os
import shutil
from pathlib import Path

def get_files(start_directory, filter_extension=None):
    for root, _, files in os.walk(start_directory):
        for file in files:
            if filter_extension is None or file.lower().endswith(filter_extension):
                yield os.path.join(root, file)

def selective_copy(source, target, file_extension=None):
    for file in get_files(source, file_extension):
        print(file)
        try:
            shutil.copy(file, target)
            print("The following file has been copied", file)
        except shutil.SameFileError:
            pass

if __name__ == "__main__":
    source_path = Path(input("Please input your source path: "))
    destination_path = Path(input("Please input your destination path: "))
    file_type = input("Please input your target file type: ")

    selective_copy(source_path, destination_path, file_type)