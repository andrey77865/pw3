from pathlib import Path
import os
import shutil
from multiprocessing.dummy import Pool

start_path = input("Input folder: ")

pool = Pool(3)

listOfDirectories = {
    "Picture": [".jpeg", ".jpg", ".gif", ".png"],
    "Video": [".wmv", ".mov", ".mp4", ".mpg", ".mpeg", ".mkv"],
    "Zip": [".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".zip"],
    "Music": [".mp3", ".msv", ".wav", ".wma"],
    "PDF": [".pdf"],
    "Documents": [".doc", ".docx", ".txt"]
}

item_Format_Dictionary = {
    file_extension: directory for directory,
    item_format_stored in listOfDirectories.items() for file_extension in item_format_stored
}


def create_folder(start_path, name):
    directory_path = Path(name)
    try:
        os.makedirs(start_path / directory_path, exist_ok=True)
    except:
        print(f"Directory '{directory_path}' already exists")


def move_file(fullpath, start_path, directory_path):
    try:
        shutil.move(fullpath, start_path / directory_path)
    except:
        print(f"File '{fullpath}' already sorted")


def sort(entry):

    for filename in entry[2]:
        full_path: Path = Path(entry[0]) / Path(filename)
        name, file_extension = os.path.splitext(full_path)

        if file_extension in item_Format_Dictionary:
            directory_path = Path(item_Format_Dictionary[file_extension])
            create_folder(start_path, directory_path)
            move_file(full_path, start_path, directory_path)
        else:
            directory_path = Path("Unknown")
            create_folder(start_path, directory_path)
            move_file(full_path, start_path, directory_path)


if __name__ == '__main__':
    pool.map(sort, os.walk(start_path))
    print('Finished')
