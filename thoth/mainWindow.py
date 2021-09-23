import sys
from PyQt5.QtCore import Qt as Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, \
    QPushButton, QFileDialog, QGroupBox, \
    QVBoxLayout, QStyleFactory, QHBoxLayout, QTreeView, QFileSystemModel, \
    QMenu

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.leftField = None
        self.contextMenu = None
        self.setStyle()
        self.setWindowTitle("file manager")
        self.createLeftField()

        leftlayout = QVBoxLayout()
        leftlayout.addWidget(self.leftField)

        model = QFileSystemModel()
        model.setRootPath("")
        self.tree = QTreeView()
        self.tree.setModel(model)
        self.tree.setRootIndex(model.index(""))
        self.tree.setColumnWidth(0, 250)
        self.tree.setAlternatingRowColors(True)
        self.tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tree.customContextMenuRequested.connect(self.treeContextMenu)

        mainlayout = QHBoxLayout()
        mainlayout.addLayout(leftlayout)
        mainlayout.addWidget(self.tree)

        w = QWidget()
        w.setLayout(mainlayout)
        self.setCentralWidget(w)

    @staticmethod
    def setStyle() -> None:
        QApplication.setStyle(QStyleFactory.create("Fusion"))

    def treeContextMenu(self, pos) -> None:
        self.contextMenu = QMenu()
        self.contextMenu.addAction(u'add').triggered.connect(self.addHandler)
        self.contextMenu.addAction(u'rename').triggered.connect(self.renameHandler)
        self.contextMenu.addAction(u'backup').triggered.connect(self.backupHandler)
        self.contextMenu.exec_(self.mapToGlobal(pos))
        self.contextMenu.show()

    def addHandler(self) -> None:
        for idx in self.tree.selectedIndexes():
            print(idx.data())

    def renameHandler(self) -> None:
        pass

    def backupHandler(self) -> None:
        pass

    def createLeftField(self) -> None:
        self.leftField = QGroupBox("File")

        OpenFileButton = QPushButton("Open File")
        OpenFileButton.clicked.connect(self.btn_chooseFile)

        OpenFolderButton = QPushButton("Open Folder")
        OpenFolderButton.clicked.connect(self.btn_chooseFolder)

        layout = QVBoxLayout()
        layout.addWidget(OpenFileButton)
        layout.addWidget(OpenFolderButton)
        layout.addStretch(1)

        self.leftField.setLayout(layout)

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
