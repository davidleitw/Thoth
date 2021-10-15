from PyQt5.QtWidgets import QFileDialog
import os

class FileManager:

    def __init__(self):
        self.Copy_Path = ""

    def set_Copy_Path(self, path) -> None:
        self.Copy_Path = path

    def get_Copy_Path(self) -> str:
        return self.Copy_Path

    def getExistingDirectory(self, folder):
        QFileDialog.getExistingDirectory(None, folder, "/")

    def getFilePath(self, model) -> str:
        return model.filePath(self.rightTree.currentIndex())

    def createfile(self, filename) -> None:
        os.system("touch " + filename)

    def createfolder(self, foldername) -> None:
        os.system("mkdir" + foldername)

    def renae(self, new_name, filename):
        os.system("mv ./" + filename + " ./" + new_name)

    def cd_Path(self, path) -> None:
        os.system("cd " + path)

    def delete(self, filename) -> None:
        os.system("rm ./" + filename)
