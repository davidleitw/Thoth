import os
from PyQt5.QtWidgets import QFileDialog
from thoth.FileManager import FileManager


class Controller:
    def __init__(self):
        self._manager = FileManager()

    def create(self, path: str, _type: str) -> bool:
        # 文件已存在的情況
        print(path)
        if os.path.exists(path):
            return False
        if _type == "file":
            self._manager.createfile(path)
        elif _type == "folder":
            self._manager.createfolder(path)
        return True
        
    def rename(self, new_name, filepath) -> bool:
        return self._manager.rename(new_name, filepath)

    def delete(self, path: str) -> None:
        self._manager.delete(path)

    def backup(self, cur_path) -> None:
        self._manager.backup(None, cur_path, self._manager.Copy_Path)
    
    def set_backup(self) -> None:
        folderPath = QFileDialog.getExistingDirectory(None, "folder", "/")
        if folderPath == "":
            return
        self._manager.set_copy_path(folderPath)
        
    def open_folder(self) -> str:
        return QFileDialog.getExistingDirectory(None, "folder", "/")