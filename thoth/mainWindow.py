import sys

from PyQt5 import QtCore
from PyQt5.QtCore import Qt as Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, \
    QPushButton, QFileDialog, QGroupBox, \
    QVBoxLayout, QStyleFactory, QHBoxLayout, QTreeView, QFileSystemModel, \
    QMenu


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.model = None
        self.leftLayout = None
        self.rightTree = None
        self.contextMenu = None

        self.loadInitialSetting()
        self.createLeftField()
        self.createRightFileTree()
        self.setMainLayout()

    def loadInitialSetting(self) -> None:
        QApplication.setStyle(QStyleFactory.create("Fusion"))
        self.setWindowTitle("file manager")

    def createLeftField(self) -> None:
        leftField = QGroupBox("toolbar")

        OpenFileButton = QPushButton("Set backup path")
        OpenFileButton.clicked.connect(self.btn_chooseFile)

        OpenFolderButton = QPushButton("Open Folder")
        OpenFolderButton.clicked.connect(self.btn_chooseFolder)

        ExitButton = QPushButton("Exit")
        ExitButton.clicked.connect(self.btn_exit)

        layout = QVBoxLayout()
        layout.addWidget(OpenFileButton)
        layout.addWidget(OpenFolderButton)
        layout.addWidget(ExitButton)
        layout.addStretch(1)

        leftField.setLayout(layout)

        self.leftLayout = QVBoxLayout()
        self.leftLayout.addWidget(leftField)

    def createRightFileTree(self) -> None:
        self.model = QFileSystemModel()
        self.model.setRootPath("")
        self.rightTree = QTreeView()
        self.rightTree.setModel(self.model)
        self.rightTree.setRootIndex(self.model.index(""))
        self.rightTree.setColumnWidth(0, 250)
        self.rightTree.setAlternatingRowColors(True)
        self.rightTree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.rightTree.customContextMenuRequested.connect(self.createTreeContextMenu)

    def setMainLayout(self) -> None:
        mainLayout = QHBoxLayout()
        mainLayout.addLayout(self.leftLayout)
        mainLayout.addWidget(self.rightTree)

        w = QWidget()
        w.setLayout(mainLayout)
        self.setCentralWidget(w)

    def createTreeContextMenu(self, pos) -> None:
        self.contextMenu = QMenu()
        self.contextMenu.addAction(u'add').triggered.connect(self.addHandler)
        self.contextMenu.addAction(u'rename').triggered.connect(self.renameHandler)
        self.contextMenu.addAction(u'delete').triggered.connect(self.deleteHandler)
        self.contextMenu.addAction(u'backup').triggered.connect(self.backupHandler)
        self.contextMenu.exec_(self.mapToGlobal(pos))
        self.contextMenu.show()

    def getFilePath(self) -> str:
        return self.model.filePath(self.rightTree.currentIndex())

    def addHandler(self) -> None:
        path = self.getFilePath()
        self.rightTree.setRootIndex(self.model.index(path))
        print(path)

    def renameHandler(self) -> None:
        path = self.getFilePath()
        print(path)

    def deleteHandler(self) -> None:
        pass

    def backupHandler(self) -> None:
        path = self.getFilePath()
        print(path)

    def btn_chooseFile(self):
        (filePath, fileType) = QFileDialog.getOpenFileName(self, "file", "/")

        if filePath == "":
            print("no file choose.")
            return

        print(filePath, fileType)

    def btn_chooseFolder(self):
        folderPath = QFileDialog.getExistingDirectory(self, "folder", "/")

        if folderPath == "":
            print("no folder")
            return
        print(folderPath)

    def btn_exit(self) -> None:
        pass
