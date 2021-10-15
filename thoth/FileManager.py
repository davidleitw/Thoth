from PyQt5.QtWidgets import QFileDialog
import os

class FileManager:

    def __init__(self):
        self.Copy_Path = ""
        self.rightTree_Path = ""

    def set_copy_path(self, path) -> None:
        self.Copy_Path = path

    def get_copy_path(self) -> str:
        return self.Copy_Path

    def createfile(self, path) -> None:
        os.system("touch " + path)

    def createfolder(self, path) -> None:
        os.system("mkdir" + path)

    def rename(self, new_name, filepath):
        n = len(filepath) - 1
        while n > 0:
            if filepath[n] == '/':
                break
            else:
                n-=1
        os.system("mv " + filepath + " " + filepath[:n + 1] + new_name)

    def delete(self, path) -> None:
        os.system("rm -r " + path)

    def backup(self, tar, src) -> None:
        os.system("cp " + src  + " " + tar)