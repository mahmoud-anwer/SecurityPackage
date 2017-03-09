

class Monoalphabetic:
    """ Frequency Information:
        E   12.51%
        T	9.25
        A	8.04
        O	7.60
        I	7.26
        N	7.09
        S	6.54
        R	6.12
        H	5.49
        L	4.14
        D	3.99
        C	3.06
        U	2.71
        M	2.53
        F	2.30
        P	2.00
        G	1.96
        W	1.92
        Y	1.73
        B	1.54
        V	0.99
        K	0.67
        X	0.19
        J	0.16
        Q	0.11
        Z	0.09
    """

    def analyse(self, plainText: str, cipherText: str) -> str:
        LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        mainKey=""
        temp = plainText.upper()
        i = 0
        while i < len(plainText):
            index = LETTERS.index(temp[i])
            mainKey = mainKey[:index] + cipherText[i] + mainKey[index+1:]
            i = i + 1
        temp = mainKey
        temp = temp.upper()
        i = 0
        while i < len(temp):
            if temp[i] == '-':
                index = LETTERS.index(temp[i - 1])
                if index == 25:
                    index = -1
                temp = temp[:i] + LETTERS[index + 1] + temp[i + 1:]
            i = i + 1
        temp = temp.lower()
        return temp

    def decrypt(self, cipherText: str, key: str) -> str:
        LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        temp = cipherText.upper()
        KEY = key.upper()
        plain = ""
        i = 0
        while i < len(cipherText):
            index = KEY.index(temp[i])
            plain += LETTERS[index]
            i = i + 1
        plain = plain.lower()
        return plain


    def encrypt(self, plainText: str, key: str) -> str:
        LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        temp = plainText.upper()
        i = 0
        EncryptedText = ""
        while i < len(plainText):
            index = LETTERS.index(temp[i])
            EncryptedText += key[index]
            i = i + 1
            EncryptedText = EncryptedText.upper()
        return EncryptedText

    def analyseUsingCharFrequency(self,  cipher: str) -> str:
        freqInfo = "ETAOINSRHLDCUMFPGWYBVKXJQZ"
        newTemp = "-" * len(cipher)
        temp = cipher.upper()
        dictionary = {}
        for letters in temp:
            dictionary[letters] = 0
        for letters in temp:
            dictionary[letters] += 1
        dictionary = sorted(dictionary.items(), reverse=True, key=lambda x: x[1])
        #print("len: ", len(temp))

        for position in range(0, len(temp)):
            #print("position: ", position)
            #print(dictionary[position])
            if position >= len(dictionary) - 1:
                break
        #print("dict: ", dictionary[1][0])
        i = 0
        while i < len(dictionary):
            #print(len(dictionary))
            #print(dictionary[i][0])
            j = 0
            while j < len(temp):
                #print("temp: ", temp[j],"dict: ", dictionary[i][0])
                if temp[j] == dictionary[i][0]:
                    #print("..", temp[j:])
                    newTemp = newTemp[:j] + freqInfo[i] + newTemp[j + 1:]
                    #print("tmp: ", temp)
                j = j + 1
            i = i + 1
        return newTemp

