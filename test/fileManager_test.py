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
        except ImportError:
            return
        
        self.fm = FileManager()
        self.tmp = '/tmp/testfolder'
        os.mkdir(self.tmp)
        print("\n")

    # 測試結束，將測試時產生的文件刪除
    def tearDown(self):
        shutil.rmtree(self.tmp)

    def test_FM_createfile(self):
        # 生成六個隨機字串
        file_set = StringGenerator("[\l\d]{10}").render_list(cnt=10, unique=True)
        for file_name in file_set:
            # 獲得路徑
            file_path = os.path.join(self.tmp, file_name)
            
            # 依序利用 FileManager api 建立文件，並且用 assert 檢查是否存在
            self.fm.createfile(file_path)
            assert os.path.exists(file_path)
            print("FM createfile: {} ---> OK".format(file_path))
            


if __name__ == '__main__':
    test = unittest.TestLoader().loadTestsFromTestCase(FileManagerTest)
    suite = unittest.TestSuite()
    suite.addTest(test)

    unittest.TextTestRunner(verbosity=2).run(suite)