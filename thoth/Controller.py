from PyQt5.QtWidgets import QFileDialog
from thoth.FileManager import FileManager as FM


class Controller:
    def __init__(self):
        self.path_record = FM()

    def set_backup(self) -> None:
        folderPath = QFileDialog.getExistingDirectory(None, "folder", "/")
        if folderPath == "":
            return
        self.path_record.set_copy_path(folderPath)
        print("copy_path: " + self.path_record.Copy_Path)

    def open_folder(self) -> None:#TODO
        folderPath = QFileDialog.getExistingDirectory(None, "folder", "/")
        if folderPath == "":
            return
        #print("open_folder: " + folderPath)

    def create_new_file(self, path) -> None:
        FM.createfile(path)

    def create_new_folder(self, path) -> None:
        FM.createfolder(path)
        pass

    def rename(self, new_name, filepath) -> bool:
        return FM.rename(new_name, filepath)

    def delete(self, path) -> None:
        FM.delete(path)

    def backup(self, cur_path) -> None:
        FM.backup(None, self.path_record.Copy_Path, cur_path)
