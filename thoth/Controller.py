from PyQt5.QtWidgets import QFileDialog

class Controller():
    def __init__(self):
        pass
        
    def set_backup(self) -> None:
        folderPath = QFileDialog.getExistingDirectory(None, "folder", "/")
        if folderPath == "":
            return
        print(folderPath)

    def open_folder(self) -> None:
        folderPath = QFileDialog.getExistingDirectory(None, "folder", "/")
        if folderPath == "":
            return
        print(folderPath)

    def create_new_file(self) -> None:
        pass

    def create_new_folder(self) -> None:
        pass

    def rename(self) -> None:
        pass

    def delete(self) -> None:
        pass

    def backup(self) -> None:
        pass
