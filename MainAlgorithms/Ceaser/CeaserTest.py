import unittest
from Ceaser import Ceaser

class CeaserTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)

        self.mainPlain1 = "meetmeaftertheparty"
        self.mainCipher1 = "phhwphdiwhuwkhsduwb".upper()
        self.mainKey1 = 3

        self.mainPlain2 = "defendtheeastwallofthecastle"
        self.mainCipher2 = "defendtheeastwallofthecastle".upper()
        self.mainKey2 = 0

        self.mainPlain3 = "defendtheeastwallofthecastle"
        self.mainCipher3 = "bcdclbrfccyqruyjjmdrfcayqrjc".upper()
        self.mainKey3 = 24

        self.newPlain = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG".lower()
        self.newCipher = "WKHTXLFNEURZQIRAMXPSVRYHUWKHODCBGRJ".upper()
        self.newKey = 3

    def CeaserTestEnc1(self):
        algorithm = Ceaser()
        cipher = algorithm.encrypt(self.mainPlain1, self.mainKey1)
        self.assertTrue(cipher == self.mainCipher1)

    def CeaserTestDec1(self):
        algorithm = Ceaser()
        plain = algorithm.decrypt(self.mainCipher1, self.mainKey1)
        self.assertTrue(plain == self.mainPlain1)

    def CeaserTestAnalysis1(self):
        algorithm = Ceaser()
        key = algorithm.analyse(self.mainPlain1 ,self.mainCipher1)
        self.assertEqual(self.mainKey1, key)

    def CeaserTestEnc2(self):
        algorithm = Ceaser()
        cipher = algorithm.encrypt(self.mainPlain2, self.mainKey2)
        self.assertTrue(cipher == self.mainCipher2)

    def CeaserTestDec2(self):
        algorithm = Ceaser()
        plain = algorithm.decrypt(self.mainCipher2, self.mainKey2)
        self.assertTrue(plain == self.mainPlain2)

    def CeaserTestAnalysis2(self):
        algorithm = Ceaser()
        key = algorithm.analyse(self.mainPlain2 ,self.mainCipher2)
        self.assertEqual(self.mainKey2, key)

    def CeaserTestEnc3(self):
        algorithm = Ceaser()
        cipher = algorithm.encrypt(self.mainPlain3, self.mainKey3)
        self.assertTrue(cipher == self.mainCipher3)

    def CeaserTestDec3(self):
        algorithm = Ceaser()
        plain = algorithm.decrypt(self.mainCipher3, self.mainKey3)
        self.assertTrue(plain == self.mainPlain2)

    def CeaserTestAnalysis3(self):
        algorithm = Ceaser()
        key = algorithm.analyse(self.mainPlain3 ,self.mainCipher3)
        self.assertEqual(self.mainKey3, key)

    def CeaserTestNewEnc1(self):
        algorithm = Ceaser()
        cipher = algorithm.encrypt(self.newPlain, self.newKey)
        self.assertTrue(cipher == self.newCipher)

    def CeaserTestNewDec1(self):
        algorithm = Ceaser()
        plain = algorithm.decrypt(self.newCipher, self.newKey)
        self.assertTrue(plain == self.mainPlain)

    def CeaserTestNewAnalysis1(self):
        algorithm = Ceaser()
        key = algorithm.analyse(self.newPlain,self.newCipher)
        self.assertEqual(self.newKey, key)


if __name__ == '__main__':
    unittest.main()
