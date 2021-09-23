import sys
from PyQt5.QtCore import Qt as Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, \
    QPushButton, QVBoxLayout, QFileDialog, QDialog, QGroupBox, \
    QVBoxLayout, QStyleFactory, QHBoxLayout, QGridLayout, QTreeView, QFileSystemModel, \
    QMenu

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self._init__Style()
        self.setWindowTitle("file manager")
        self.createLeftFunctionField()

        mainlayout = QHBoxLayout()

        leftLayout = QVBoxLayout()
        leftLayout.addWidget(self.leftFunctionField)

        model = QFileSystemModel()
        model.setRootPath("")
        self.tree = QTreeView()
        self.tree.setModel(model)
        self.tree.setRootIndex(model.index(""))
        self.tree.setColumnWidth(0, 250)
        self.tree.setAlternatingRowColors(True)
        self.tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tree.customContextMenuRequested.connect(self.treeContextMenu)

        mainlayout.addLayout(leftLayout)
        mainlayout.addWidget(self.tree)
        w = QWidget()
        w.setLayout(mainlayout)
        self.setCentralWidget(w)

    @staticmethod
    def _init__Style() -> None:
        QApplication.setStyle(QStyleFactory.create("Fusion"))

    def treeContextMenu(self, pos):
        self.contextMenu = QMenu()
        self.actionA = self.contextMenu.addAction(u'Method A')
        self.actionB = self.contextMenu.addAction(u'Method B')
        self.actionA.triggered.connect(self.actionHandler)
        self.contextMenu.exec_(self.mapToGlobal(pos))
        self.contextMenu.show()

    def actionHandler(self):
        for idx in self.tree.selectedIndexes():
            print(idx.data())

    def createLeftFunctionField(self):
        self.leftFunctionField = QGroupBox("File")

        OpenFileButton = QPushButton("Open File")
        OpenFolderButton = QPushButton("Open Folder")
        OpenFileButton.clicked.connect(self.btn_chooseFile)
        OpenFolderButton.clicked.connect(self.btn_chooseFolder)

        layout = QVBoxLayout()
        layout.addWidget(OpenFileButton)
        layout.addWidget(OpenFolderButton)
        layout.addStretch(1)

        self.leftFunctionField.setLayout(layout)

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
