import os
import shutil
from pathlib import Path
from PyQt5.QtWidgets import QFileDialog

class FileManager:
    def __init__(self):
        self.Copy_Path = ""

    def set_copy_path(self, path) -> None:
        self.Copy_Path = path

    def get_copy_path(self) -> str:
        return self.Copy_Path

    def createfile(self, path) -> None:
        Path(path).touch()

    def createfolder(self, path) -> None:
        os.mkdir(path)
        
    def rename(self, new_name, filepath) -> bool:
        prefix = os.path.split(filepath)[0]
        new_filepath = os.path.join(prefix, new_name)
        if not os.path.isfile(new_filepath):
            try:
                os.rename(filepath, new_filepath)
                return True
            except:
                print("PermissionError")
        return False
        
    def delete(self, path) -> bool:
        try:
            if os.path.isfile(path):
                os.remove(path)
            else:
                shutil.rmtree(path)
            return True
        except PermissionError:
            print("PermissionError")
            return False

    def backup(self, dst, src) -> None:
        print(src + " " + dst)
        if os.path.isfile(src):
            shutil.copy(src, dst)
        else:
            dir_name = os.path.basename(dst)
            new_path = os.path.join(src, dir_name) # a/b
            if os.path.exists(new_path):
                print('path exist.')
                # shutil.rmtree(new_path)
            else:    
                shutil.copytree(dst, new_path)
