import unittest
from AgileWebDev_Assignment3.TexasPoker import CompareCard
class MyclassTest(unittest.TestCase):
    def setUp(self):
        print('开始测试====='+self.id())
        self.cls = CompareCard()
        pass
    def tearDown(self) -> None:
        print('结束测试====='+self.id())
        pass

    def test1(self):
        ret = self.cls.compare('2H 3D 5S 9C KD', '2C 3H 4S 8C AH')
        self.assertEqual(ret,'White wins')
    def test2(self):
        ret = self.cls.compare('2H 4S 4C 2D 4H', '2S 8S AS QS 3S')
        self.assertEqual(ret,'Black wins')
    def test3(self):
        ret = self.cls.compare('2H 3D 5S 9C KD', '2C 3H 4S 8C KH')
        self.assertEqual(ret,'Black wins')
    def test4(self):
        ret = self.cls.compare('2H 3D 5S 9C KD', '2H 3D 5S 9C KD')
        self.assertEqual(ret,'Tie game')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MyclassTest('test1'))
    suite.addTest(MyclassTest('test2'))
    suite.addTest(MyclassTest('test3'))
    suite.addTest(MyclassTest('test4'))
    runner = unittest.TextTestRunner()
    runner.run(suite)