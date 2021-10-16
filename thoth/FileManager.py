from PyQt5.QtWidgets import QFileDialog
import os
import shutil
from pathlib import Path

class FileManager:

    def __init__(self):
        self.Copy_Path = ""
        self.rightTree_Path = ""

    def set_copy_path(self, path) -> None:
        self.Copy_Path = path

    def get_copy_path(self) -> str:
        return self.Copy_Path

    def createfile(self, path) -> None:
        Path(path).touch()

    def createfolder(self, path) -> None:
        os.mkdir(path)

    @staticmethod
    def rename(new_name, filepath) -> bool:
        prefix = os.path.split(filepath)[0]
        new_filepath = os.path.join(prefix, new_name)
        print(filepath, new_filepath)
        if not os.path.isfile(new_filepath):
            os.rename(filepath, new_filepath)
            return True
        return False
        

    @staticmethod
    def delete(path) -> None:
        if os.path.isfile(path):
            os.remove(path)
        else:
            shutil.rmtree(path)

    def backup(self, dst, src) -> None:
        if os.path.isfile(src):
            shutil.copy(src, dst)
        else:
            shutil.copytree(src, dst)
        print(src + " " + dst)
