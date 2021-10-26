import os
from PyQt5.QtWidgets import QFileDialog
from thoth.FileManager import FileManager


class Controller:
    def __init__(self):
        self._manager = FileManager()

    def create(self, path: str, _type: str) -> bool:
        # 文件已存在的情況
        if os.path.exists(path):
            return False
        if _type == "file":
            self._manager.createfile(path)
        elif _type == "folder":
            self._manager.createfolder(path)
        return True
        
    def rename(self, new_name: str, filepath: str) -> bool:
        return self._manager.rename(new_name, filepath)

    def delete(self, path: str) -> None:
        self._manager.delete(path)

    def backup(self, filepath: str) -> None:
        self._manager.backup(filepath)
    
    def set_backup(self, path: str="/") -> None:
        folderPath = QFileDialog.getExistingDirectory(None, "folder", path)
        if folderPath == "":
            return
        self._manager.set_backup_path(folderPath)
        
    def open_folder(self, path: str="/") -> str:
        return QFileDialog.getExistingDirectory(None, "folder", path)