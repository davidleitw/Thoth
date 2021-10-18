import os
import sys
import shutil
import unittest
from strgen import StringGenerator

sys.path.append('../thoth')

class FileManagerTest(unittest.TestCase):
    # 測試前，在/tmp底下創立測試資料夾
    def setUp(self):
        try:
            from thoth.FileManager import FileManager
            self.fm = FileManager()
        except ImportError:
            return
        
        self.backup_path = '/tmp/backup'
        self.tmp_path = '/tmp/testfolder'
        os.mkdir(self.tmp_path)
        os.mkdir(self.backup_path)
        
    # 測試結束，將測試時產生的文件刪除
    def tearDown(self):
        shutil.rmtree(self.tmp_path)
        shutil.rmtree(self.backup_path)

    def test_FM_createfile(self):
        print('\n=== test fileManager.createfile function ===\n')
        # 生成 10 個隨機字串
        file_set = StringGenerator("[\l\d]{10}").render_list(cnt=10, unique=True)
        for file_name in file_set:
            # 獲得路徑
            file_path = os.path.join(self.tmp_path, file_name)
            
            # 依序利用 FileManager api 建立文件，並且用 assert 檢查是否存在
            self.fm.createfile(file_path)
            self.assertTrue(os.path.isfile(file_path))
            print("FM createfile: {} ---> OK".format(file_path))

    def test_FM_createfolder(self):
        print('\n=== test fileManager.createfolder function ===\n')
        folder_set = StringGenerator("[\l\d]{10}").render_list(cnt=10, unique=True)
        for folder_name in folder_set:
            folder_path = os.path.join(self.tmp_path, folder_name)

            self.fm.createfolder(folder_path)
            self.assertTrue(os.path.isdir(folder_path))
            print("FM createfolder: {} ---> OK".format(folder_path))

    def test_FM_rename(self):
        print('\n=== test fileManager rename function ===\n')    

    def test_FM_delete(self):
        print('\n=== test fileManager delete function ===\n')

    def test_FM_backup(self):
        print('\n=== test fileManager backup function ===\n')

if __name__ == '__main__':
    # test = unittest.TestLoader().loadTestsFromTestCase(FileManagerTest)
    # suite = unittest.TestSuite()
    # suite.addTest(test)

    # unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()