from PyQt5 import QtCore
from PyQt5.QtCore import QCoreApplication, Qt as Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QStyle, QWidget, \
    QPushButton, QGroupBox, \
    QVBoxLayout, QStyleFactory, QHBoxLayout, QTreeView, QFileSystemModel, \
    QMenu, QLineEdit, QInputDialog
import ntpath, os
from thoth.Controller import Controller

class MainWindow(QMainWindow):
    def __init__(self, parent=None, winDefaultPath: str ="/", 
                                    openDefaultPath: str="/", backupDefaultPath: str="/"):
        super(MainWindow, self).__init__(parent)
        self.model = None
        self.prePath = "/"
        self.leftLayout = None
        self.rightTree = None
        self.contextMenu = None
        self.controller = Controller()
        self.winDefault = winDefaultPath
        self.opnDefault = openDefaultPath
        self.bupDefault = backupDefaultPath

        self.loadInitialSetting()
        self.createLeftField()
        self.createRightFileTree()
        self.setMainLayout()

    def loadInitialSetting(self) -> None:
        QApplication.setStyle(QStyleFactory.create("Fusion"))
        self.setWindowTitle("file manager")

    def createLeftField(self) -> None:
        SetupButton = QPushButton(" Set backup path")
        SetupButton.setIcon(self.style().standardIcon(getattr(QStyle, 'SP_DirOpenIcon')))
        SetupButton.setStyleSheet("QPushButton { text-align: left; }")
        SetupButton.clicked.connect(self.setbackupHandler)
        
        OpenFolderButton = QPushButton(" Open Folder")
        OpenFolderButton.setIcon(self.style().standardIcon(getattr(QStyle, 'SP_DirOpenIcon')))
        OpenFolderButton.setStyleSheet("QPushButton { text-align: left; }")
        OpenFolderButton.clicked.connect(self.openFolderHandler)
        
        BackButton = QPushButton(" Back")
        BackButton.setIcon(self.style().standardIcon(getattr(QStyle, 'SP_FileDialogBack')))
        BackButton.setStyleSheet("QPushButton { text-align: left; }")
        BackButton.clicked.connect(self.backHandler)

        ExitButton = QPushButton(" Exit")
        ExitButton.setIcon(self.style().standardIcon(getattr(QStyle, 'SP_DialogCloseButton')))
        ExitButton.setStyleSheet("QPushButton { text-align: left; }")
        ExitButton.clicked.connect(QCoreApplication.instance().quit)

        layout = QVBoxLayout()
        layout.addWidget(SetupButton)
        layout.addWidget(OpenFolderButton)
        layout.addWidget(BackButton)
        layout.addWidget(ExitButton)
        layout.addStretch(1)
        
        leftField = QGroupBox("toolbar")
        leftField.setLayout(layout)

        self.leftLayout = QVBoxLayout()
        self.leftLayout.addWidget(leftField)

    def createRightFileTree(self) -> None:
        self.model = QFileSystemModel()
        self.model.setRootPath("")
        self.rightTree = QTreeView()
        self.rightTree.setModel(self.model)
        self.rightTree.setRootIndex(self.model.index(self.winDefault))
        self.rightTree.setColumnWidth(0, 250)
        self.rightTree.setAlternatingRowColors(True)
        self.rightTree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.rightTree.customContextMenuRequested.connect(self.createTreeContextMenu)

    def createTreeContextMenu(self, pos: QtCore.QPoint) -> None:
        self.contextMenu = QMenu()
        if os.path.isdir(self.getFilePath()):
            self.contextMenu.addAction(u'New file').triggered.connect(self.createNewFileHandler)
            self.contextMenu.addAction(u'New folder').triggered.connect(self.createNewFolderHandler)
        
        self.contextMenu.addAction(u'Rename').triggered.connect(self.renameHandler)
        self.contextMenu.addAction(u'Delete').triggered.connect(self.deleteHandler)
        self.contextMenu.addAction(u'Backup').triggered.connect(self.backupHandler)
        self.contextMenu.exec_(self.mapToGlobal(pos))
        self.contextMenu.show()

    def setMainLayout(self) -> None:
        mainLayout = QHBoxLayout()
        mainLayout.addLayout(self.leftLayout)
        mainLayout.addWidget(self.rightTree)

        w = QWidget()
        w.setLayout(mainLayout)
        self.setCentralWidget(w)

    def getFilePath(self) -> str:
        return self.model.filePath(self.rightTree.currentIndex())

    def openFolderHandler(self) -> None:
        self.prePath = self.model.filePath(self.rightTree.rootIndex()) # 將前一次操作的目錄存起來，供上一頁功能使用
        filepath = self.controller.open_folder(self.opnDefault)
        if filepath != '' and os.path.isdir(filepath):
            self.rightTree.setRootIndex(self.model.index(filepath))

    def setbackupHandler(self):
        self.controller.set_backup(self.bupDefault)

    # 上一頁功能
    def backHandler(self) -> None:
        self.rightTree.setRootIndex(self.model.index(self.prePath))

    def createNewFileHandler(self) -> None:
        basePath = self.getFilePath()
        newFileName, ok = QInputDialog.getText(self, "create new file", "file name: ", QLineEdit.Normal, "")
        if ok and newFileName != '':
            self.controller.create(os.path.join(basePath, newFileName), "file")
        self.contextMenu.clear()
        self.contextMenu.close()

    def createNewFolderHandler(self) -> None:
        basePath = self.getFilePath()
        newFolderName, ok = QInputDialog.getText(self, "create new folder", "folder name: ", QLineEdit.Normal, "")
        if ok and newFolderName != '':
            self.controller.create(os.path.join(basePath, newFolderName), "folder")
        self.contextMenu.clear()
        self.contextMenu.close()

    def renameHandler(self) -> None:
        filepath = self.getFilePath()

        old_name = ntpath.basename(filepath)
        newFileName, ok = QInputDialog.getText(self, "rename", "file / folder name: ", QLineEdit.Normal, old_name)
        if ok and newFileName != '':
            self.controller.rename(newFileName, filepath)
        self.contextMenu.clear()
        self.contextMenu.close()

    def deleteHandler(self) -> None:
        filepath = self.getFilePath()
        self.controller.delete(filepath)
        self.contextMenu.clear()
        self.contextMenu.close()

    # 備份功能
    def backupHandler(self) -> None:
        filepath = self.getFilePath()
        self.controller.backup(filepath)
        self.contextMenu.clear()
        self.contextMenu.close()

    
        