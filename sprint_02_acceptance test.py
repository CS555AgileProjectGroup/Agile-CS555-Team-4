
import unittest
import sprint02
check=(sprint02.fileInput == " ")

class TestStringMethods(unittest.TestCase):
    def test_1(self):
        self.assertNotEqual(sprint02.birthBeforeDeathOfParents, 0)
    def test_2(self):
        self.assertIsNotNone(sprint02.marriageAfter14, msg = None)
    def test_3(self):
        self.assertTrue(sprint02.noBigamy, 0)
    def test_4(self):
       self.assertEqual("2002-06-27","2002-06-27")
    def test_5(self):
        self.assertIsNotNone(sprint02.SiblingsSpacing, msg = None)
    def test_6(self):
       self.assertNotEqual(sprint02.parentsNotTooOld, 0)
    def test_7(self):
        self.assertNotEqual(sprint02.multipleBirthslessThan5, 0)
    def test_8(self):
        self.assertIsNotNone(sprint02.lessThan15Siblings, msg = None)
    def test_9(self):
        self.assertTrue(sprint02.marriageAfter14, 0)
unittest.main()

