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
        n = len(filepath) - 1
        while n > 0:
            if filepath[n] == '/':
                break
            else:
                n-=1

        current_list = [i for i in os.listdir(filepath[:n + 1])]
        flag = True
        for i in current_list:
            print(i)
            if i == new_name:
                flag = False
                break;

        print(flag)

        if flag:
            os.rename(filepath, filepath[:n + 1] + new_name)
            return flag

        return flag

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
