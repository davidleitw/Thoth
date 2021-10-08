# Thoth

## 待辦事項
- function 實現(名稱待訂)
    - Toolbar:
        - Open Folder():開啟右邊資料夾樹
        - Set backup path():設定一鍵備份位置
    - 右鍵一下(開啟功能選單顯示以下功能):
        - New():新增檔案
        - Rename():更改檔案名
        - Delete():刪除檔案
        - Backup():一鍵備份
    - 左鍵兩下:
        - 顯示屬性():顯示檔案細項
- 排版設計
    - 設計各個功能擺放位置與整體設計

## 程式架構
三檔案
- MainWindow.py
    - 宣告各個元件
    - 擺放各個元件位置
    - 綁定各個元件功能(function)
- Controller.py
    - 定義各個 funcion 的內容
    - 使用 FileManager 的動作(FileManager.function())進行定義
- FileManager.py
    - 定義各個實際操作檔案的動作(function)

![](https://i.imgur.com/HiSMRnW.png)
回到計劃書: https://hackmd.io/I3QZ3Iv3SYuTxdIuLGQI5Q

### reference

- [pyqt_example](https://github.com/pyqt/examples/tree/_/src/02%20PyQt%20Widgets)
- [pyqt QTreeView](https://www.cxyzjd.com/article/BigTail_cat/81172531)
- [PyQt5 右鍵菜單Context Menu 彈出的方法](https://www.twblogs.net/a/5cd75629bd9eee6726c9c19a)
- [PYQT5(14)pyqt5 QTreeWidget使用集锦(如右键菜单)](https://www.jianshu.com/p/4ecb8dd775f4)
- [QTreeview change icon on row Icon click](https://stackoverflow.com/questions/45035515/qtreeview-change-icon-on-row-icon-click)
- [Layout management](https://www.pythonguis.com/tutorials/pyqt-layouts/)
- [PyQt5 QFileDialog](https://blog.csdn.net/humanking7/article/details/80546728)
- [how to have a directory dialog](https://stackoverflow.com/questions/4286036/how-to-have-a-directory-dialog)