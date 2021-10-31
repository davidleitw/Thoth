import os
import sys
import shutil
import unittest
from pathlib import Path
from strgen import StringGenerator



class FileManagerTest(unittest.TestCase):
    # 測試前，在/tmp底下創立測試資料夾
    def setUp(self):
        try:
            sys.path.append('../thoth')
            from thoth.FileManager import FileManager
            self.fm = FileManager()
        except ImportError:
            print("Import Error, new path = {}".format(os.getcwd()))
            return

    @classmethod
    def setUpClass(cls):
        cls.test_backup_path = 'C:/tmp/testBackup/'
        cls.test_tmp_path = 'C:/tmp/testFolder/'
        os.mkdir(cls.test_tmp_path)
        os.mkdir(cls.test_backup_path)

    @classmethod
    def tearDownClass(cls):
       shutil.rmtree(cls.test_tmp_path)
       shutil.rmtree(cls.test_backup_path)

#

    def test_FM_createfile_Method_001(self):#創相同名稱的檔案10次
        print('\n=== test fileManager.createfile function ===\n')
        # 生成 10 個隨機字串
        file_name = StringGenerator("[\l\d]{16}").render()
        for i in range(1,10):
            # 獲得路徑
            file_path = os.path.join(FileManagerTest.test_tmp_path, file_name)
            file_path = Path(file_path).as_posix()
            # 依序利用 FileManager api 建立文件，並且用 assert 檢查是否存在
            print(self.fm.createfile(file_path))
            print(file_path)
            self.assertTrue(os.path.isfile(file_path))
            print("FM createfile: {} ---> OK".format(file_path))


    def test_FM_createfile_Method_002(self):#創不同名稱的檔案10次
        print('\n=== test fileManager.createfile function ===\n')
        # 生成 10 個隨機字串
        file_set = StringGenerator("[\l\d]{16}").render_list(cnt=10, unique=True)
        for file_name in file_set:
            # 獲得路徑
            file_path = os.path.join(FileManagerTest.test_tmp_path, file_name)
            file_path = Path(file_path).as_posix()

            # 依序利用 FileManager api 建立文件，並且用 assert 檢查是否存在
            self.fm.createfile(file_path)
            self.assertTrue(os.path.isfile(file_path))
            print("FM createfile: {} ---> OK".format(file_path))
            
    def test_FM_createfile_Method_003(self):#創空名稱的檔案
        print('\n=== test fileManager.createfile function ===\n')
        #空名稱
        file_name = ""
        file_path = os.path.join(FileManagerTest.test_tmp_path, file_name)
        # 依序利用 FileManager api 建立文件，並且用 assert 檢查是否存在
        self.fm.createfile(file_path)
        self.assertFalse(os.path.isfile(file_path))
        print("FM createfile: {} ---> OK".format(file_path))
            
    def test_FM_createfile_Method_004(self):#創不法字元名稱的檔案
        print('\n=== test fileManager.createfile function ===\n')
        # 不法字元名稱
        file_name = "?><\/:"
        file_path = os.path.join(FileManagerTest.test_tmp_path, file_name)
        file_path = Path(file_path).as_posix()

        # 依序利用 FileManager api 建立文件，並且用 assert 檢查是否存在
        vaild = self.fm.createfile(file_path)
        if not vaild:
            self.assertFalse(os.path.isfile(file_path))
        print("FM createfile: {} ---> OK".format(file_path))

    def test_FM_createfile_Method_005(self):# 生成國外語言檔案
        print('\n=== test fileManager.createfile function ===\n')
        # 生成國外語言
        file_set = ["నిర్ధారించండిA","батлахA","คอนเฟิร์มA"]
        for file_name in file_set:
            # 獲得路徑
            file_path = os.path.join(FileManagerTest.test_tmp_path, file_name)
            file_path = Path(file_path).as_posix()
            # 依序利用 FileManager api 建立文件，並且用 assert 檢查是否存在
            self.fm.createfile(file_path)
            self.assertTrue(os.path.isfile(file_path))
            print("FM createfile: {} ---> OK".format(file_path))
    
    def test_FM_createfolder_Method_006(self): # 創不同名稱的資料夾
        print('\n=== test fileManager.createfolder function ===\n')
        # 生成 10 個隨機字串
        folder_set = StringGenerator("[\l\d]{16}").render_list(cnt=10, unique=True)
        for folder_name in folder_set:
            # 獲得路徑
            folder_path = os.path.join(FileManagerTest.test_tmp_path, folder_name)
            folder_path = Path(folder_path).as_posix()

            self.fm.createfolder(folder_path)
            self.assertTrue(os.path.isdir(folder_path))
            print("FM createfolder: {} ---> OK".format(folder_path))
            
    def test_FM_createfolder_Method_007(self):# 創相同名稱的資料夾
        print('\n=== test fileManager.createfolder function ===\n')
        # 生成 10 個隨機字串
        folder_name = StringGenerator("[\l\d]{16}").render()
        for i in range(1,10):
            # 獲得路徑
            folder_path = os.path.join(FileManagerTest.test_tmp_path, folder_name)
            if os.path.exists(folder_path):
                if self.fm.createfolder(folder_path):
                    self.assertTrue(os.path.isdir(folder_path))
            print("FM createfolder: {} ---> OK".format(folder_path))

    def test_FM_createfolder_Method_008(self):#創空名稱資料夾
        print('\n=== test fileManager.createfolder function ===\n')
        #空名稱
        folder_name = ""
            # 獲得路徑
        folder_path = os.path.join(FileManagerTest.test_tmp_path, folder_name)
        if folder_name != "":
            self.fm.createfolder(folder_path)
            self.assertTrue(os.path.isdir(folder_path))
        print("FM createfolder: {} ---> OK".format(folder_path))


    def test_FM_createfolder_Method_009(self):#創不法字元資料夾
        print('\n=== test fileManager.createfolder function ===\n')
        #不法字元名稱
        folder_name = "?><\/:*|"
            # 獲得路徑
        folder_path = os.path.join(FileManagerTest.test_tmp_path, folder_name)

        if self.fm.createfolder(folder_path):
            self.assertTrue(os.path.isdir(folder_path))
        else:
            self.assertFalse(os.path.isdir(folder_path))
        print("FM createfolder: {} ---> OK".format(folder_path))


    def test_FM_createfolder_Method_010(self):#創國外語言資料夾
        print('\n=== test fileManager.createfolder function ===\n')
        # 生成國外語言
        folder_set = ["నిర్ధారించండAXి","батлахAX","คอนเฟิร์มAX"]

        for folder_name in folder_set:
            # 獲得路徑
            folder_path = os.path.join(FileManagerTest.test_tmp_path, folder_name)

            self.fm.createfolder(folder_path)
            self.assertTrue(os.path.isdir(folder_path))
            print("FM createfolder: {} ---> OK".format(folder_path))
            
    def test_FM_rename_Method_011(self):#正常修改名稱 創test 改test123
        print('\n=== test fileManager.rename function ===\n')
        # 生成test檔案
        initialname="test"
        file_path = os.path.join(FileManagerTest.test_tmp_path, initialname)
        self.fm.createfile(file_path)

        #改名後的名稱
        newname = "test123"
        # 獲得路徑
        path = os.path.join(FileManagerTest.test_tmp_path + "/test")

        #改名
        self.fm.rename(newname, path)
        self.assertTrue(os.path.isfile(os.path.join(FileManagerTest.test_tmp_path,newname)))

    def test_FM_rename_Method_012(self):#創test 改空的名稱
        print('\n=== test fileManager.rename function ===\n')
        # 生成test檔案
        initialname="test"
        file_path = os.path.join(FileManagerTest.test_tmp_path, initialname)
        self.fm.createfile(file_path)

        #改名後的名稱
        newname = ""
        # 獲得路徑
        path = os.path.join(FileManagerTest.test_tmp_path + "/test")

        #改名
        self.fm.rename(newname, path)
        self.assertFalse(os.path.isfile(os.path.join(FileManagerTest.test_tmp_path,newname)))

    def test_FM_rename_Method_013(self):#創test 改不法字元
        print('\n=== test fileManager.rename function ===\n')
        # 生成test檔案
        initialname="test"
        file_path = os.path.join(FileManagerTest.test_tmp_path, initialname)
        self.fm.createfile(file_path)

        #改名後的名稱
        newname = "></\|?"
        # 獲得路徑
        path = os.path.join(FileManagerTest.test_tmp_path + "/test")

        #改名
        if self.fm.rename(newname, path):
            self.assertTrue(os.path.isfile(os.path.join(FileManagerTest.test_tmp_path,newname)))



    def test_FM_rename_Method_014(self):#創test 改國外名稱
        print('\n=== test fileManager.rename function ===\n')
        # 生成test檔案
        initialname="test"
        file_path = os.path.join(FileManagerTest.test_tmp_path, initialname)
        self.fm.createfile(file_path)

        #改名後的名稱
        newname = "నిర్ధారించండిB"
        # 獲得路徑
        path = os.path.join(FileManagerTest.test_tmp_path + "/test")

        #改名
        if self.fm.rename(newname, path):
            self.assertTrue(os.path.isfile(os.path.join(FileManagerTest.test_tmp_path,newname)))


    def test_FM_rename_Method_015(self):#創test 改test123 100次
        print('\n=== test fileManager.rename function ===\n')
        # 生成test檔案
        initialname="test"
        file_path = os.path.join(FileManagerTest.test_tmp_path, initialname)
        self.fm.createfile(file_path)

        #改名後的名稱
        newname = "test123"
        # 獲得路徑
        path = os.path.join(FileManagerTest.test_tmp_path + "/test")

        #改名
        for i in range(1,100):
            self.fm.rename(newname, path)
            self.assertTrue(os.path.isfile(os.path.join(FileManagerTest.test_tmp_path,newname)))
            
            
    def test_FM_rename_Method_016(self):#創test 改成長字串的名稱
        print('\n=== test fileManager.rename function ===\n')
        # 生成test檔案
        initialname="test"
        file_path = os.path.join(FileManagerTest.test_tmp_path, initialname)
        self.fm.createfile(file_path)

        #改名後的名稱
        newname = "012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789"
        # 獲得路徑
        path = os.path.join(FileManagerTest.test_tmp_path + "/test")

        #改名
        self.fm.rename(newname, path)
        self.assertTrue(os.path.isfile(os.path.join(FileManagerTest.test_tmp_path,newname)))
        
    def test_FM_delete_Method_017(self):#創test 刪掉
        print('\n=== test fileManager.rename function ===\n')
        # 生成test檔案
        name = "test"
        file_path = os.path.join(FileManagerTest.test_tmp_path, name)
        self.fm.createfile(file_path)



        # 刪除
        self.fm.delete(file_path)
        self.assertFalse(os.path.isfile(file_path))

    def test_FM_delete_Method_018(self):  # 刪掉不存在的test
        print('\n=== test fileManager.rename function ===\n')
        # 生成test檔案
        name = "test"
        file_path = os.path.join(FileManagerTest.test_tmp_path, name)
        self.fm.createfile(file_path)

        # 刪除
        self.fm.delete(file_path)
        self.assertFalse(os.path.isfile(file_path))


    def test_FM_delete_Method_019(self):#創test 然後刪掉他 但我沒刪掉
        print('\n=== test fileManager.rename function ===\n')
        # 生成test檔案
        file_set = StringGenerator("[\l\d]{16}").render_list(cnt=10, unique=True)
        for file_name in file_set:
            # 獲得路徑
            file_path = os.path.join(FileManagerTest.test_tmp_path, file_name)

            # 依序利用 FileManager api 建立文件，並且用 assert 檢查是否存在
            self.fm.createfile(file_path)

        # 刪除
        for file_name in file_set:
            file_path = os.path.join(FileManagerTest.test_tmp_path, file_name)
            self.fm.delete(file_path)
            self.assertFalse(os.path.isfile(file_path))




    """

    def test_FM_delete(self):
        print('\n=== test fileManager delete function ===\n')

    def test_FM_backup(self):
        print('\n=== test fileManager backup function ===\n')
    """
if __name__ == '__main__':
    # test = unittest.TestLoader().loadTestsFromTestCase(FileManagerTest)
    # suite = unittest.TestSuite()
    # suite.addTest(test)

    # unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()
