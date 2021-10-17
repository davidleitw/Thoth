import os
import shutil
from pathlib import Path
from PyQt5.QtWidgets import QFileDialog

class FileManager:
    def __init__(self):
        self.backup_path = ""

    def set_backup_path(self, path: str) -> None:
        self.backup_path = path

    def get_backup_path(self) -> str:
        return self.backup_path

    def createfile(self, path: str) -> None:
        Path(path).touch()

    def createfolder(self, path: str) -> None:
        os.mkdir(path)
        
    def rename(self, new_name: str, filepath: str) -> bool:
        prefix = os.path.split(filepath)[0]
        new_filepath = os.path.join(prefix, new_name)
        if not os.path.isfile(new_filepath):
            try:
                os.rename(filepath, new_filepath)
                return True
            except:
                print("PermissionError")
        return False
        
    def delete(self, path: str) -> bool:
        try:
            if os.path.isfile(path):
                os.remove(path)
            else:
                shutil.rmtree(path)
            return True
        except PermissionError:
            return False

    def backup(self, path: str) -> bool:
        # 沒有設置備份路徑的情況
        if self.backup_path == "":
            return False

        if os.path.isfile(path):
            try:
                shutil.copy(path, self.backup_path)
            except PermissionError:
                return False
        else:
            new_path = os.path.join(self.backup_path, os.path.basename(path))
            try:
                if os.path.exists(new_path):
                    return False
                shutil.copytree(path, new_path)
            except PermissionError:
                return False
        return True
