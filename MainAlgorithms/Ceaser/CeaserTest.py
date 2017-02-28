import unittest
from Ceaser import Ceaser

class CeaserTest(unittest.TestCase):
    mainPlain1 = "meetmeaftertheparty"
    mainCipher1 = "phhwphdiwhuwkhsduwb".upper()
    mainKey1 = 3

    mainPlain2 = "defendtheeastwallofthecastle"
    mainCipher2 = "defendtheeastwallofthecastle".upper()
    mainKey2 = 0

    mainPlain3 = "defendtheeastwallofthecastle"
    mainCipher3 = "bcdclbrfccyqruyjjmdrfcayqrjc".upper()
    mainKey3 = 24

    newPlain = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG".lower()
    newCipher = "WKHTXLFNEURZQIRAMXPSVRYHUWKHODCBGRJ".upper()
    newKey = 3

    def test_CeaserTestEnc1(self):
        algorithm = Ceaser()
        cipher = algorithm.encrypt(self.mainPlain1, self.mainKey1)
        self.assertTrue(cipher == self.mainCipher1)

    def test_CeaserTestDec1(self):
        algorithm = Ceaser()
        plain = algorithm.decrypt(self.mainCipher1, self.mainKey1)
        self.assertTrue(plain == self.mainPlain1)

    def test_CeaserTestAnalysis1(self):
        algorithm = Ceaser()
        key = algorithm.analyse(self.mainPlain1 ,self.mainCipher1)
        self.assertEqual(self.mainKey1, key)

    def test_CeaserTestEnc2(self):
        algorithm = Ceaser()
        cipher = algorithm.encrypt(self.mainPlain2, self.mainKey2)
        self.assertTrue(cipher == self.mainCipher2)

    def test_CeaserTestDec2(self):
        algorithm = Ceaser()
        plain = algorithm.decrypt(self.mainCipher2, self.mainKey2)
        self.assertTrue(plain == self.mainPlain2)

    def test_CeaserTestAnalysis2(self):
        algorithm = Ceaser()
        key = algorithm.analyse(self.mainPlain2 ,self.mainCipher2)
        self.assertEqual(self.mainKey2, key)

    def test_CeaserTestEnc3(self):
        algorithm = Ceaser()
        cipher = algorithm.encrypt(self.mainPlain3, self.mainKey3)
        self.assertTrue(cipher == self.mainCipher3)

    def test_CeaserTestDec3(self):
        algorithm = Ceaser()
        plain = algorithm.decrypt(self.mainCipher3, self.mainKey3)
        self.assertTrue(plain == self.mainPlain2)

    def test_CeaserTestAnalysis3(self):
        algorithm = Ceaser()
        key = algorithm.analyse(self.mainPlain3 ,self.mainCipher3)
        self.assertEqual(self.mainKey3, key)

    def test_CeaserTestNewEnc1(self):
        algorithm = Ceaser()
        cipher = algorithm.encrypt(self.newPlain, self.newKey)
        self.assertTrue(cipher == self.newCipher)

    def test_CeaserTestNewDec1(self):
        algorithm = Ceaser()
        plain = algorithm.decrypt(self.newCipher, self.newKey)
        self.assertTrue(plain == self.mainPlain)

    def test_CeaserTestNewAnalysis1(self):
        algorithm = Ceaser()
        key = algorithm.analyse(self.newPlain,self.newCipher)
        self.assertEqual(self.newKey, key)


if __name__ == '__main__':
    unittest.main()
