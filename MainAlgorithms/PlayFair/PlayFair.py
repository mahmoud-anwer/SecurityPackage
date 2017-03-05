

class PlayFair:
    """
    The most common diagrams in english (sorted): TH, HE, AN, IN, ER, ON, RE, ED, ND, HA, AT, EN, ES, OF, NT, EA, TI, TO, IO, LE, IS, OU, AR, AS, DE, RT, VE
    """
    def analyse(self, plainText: str) -> str:
        raise NotImplementedError

    # Don't implement that
    #def analyse(self, plainText: str, cipherText: str) -> str:
        #raise NotImplementedError

    def decrypt(self, cipherText: str, key:str ) -> str:
        #raise NotImplementedError
        checked = {}
        alphabet = "abcdefghiklmnopqrstuvwxyz"
        for i in range(25):
            checked[alphabet[i]]= False

        matrix = [[0 for row in range(5)] for column in range(5) ]
        db = key.lower() + alphabet.lower()
        ciphertext = cipherText.lower()

        row = 0
        column = 0
        for letter in db:
            if row < 5 and column < 5:
                if checked[letter] is False and letter != 'j':
                    matrix[row][column] = letter
                    checked[letter] = True
                    column = column +1
                elif letter == 'j' and checked['i'] is False:
                    matrix[row][column] = 'i'
                    checked['i'] = True
                    column = column


                if column == 5:
                    row = row+1
                    column = 0

        if len(ciphertext)%2 != 0 :
            plaintext = ciphertext + 'x'

        length = int(len(ciphertext)/2)
        ct=["" for letter in range(length)]
        pt=["" for letter in range(length)]
        count = 0
        for i in range(length):
            ct[i]=ciphertext[count] + ciphertext[count+1]
            count = count+2

        for letter in range(length):
            str = ct[letter]
            for row in range(5):
                for column in range(5):
                    if str[0] == matrix[row][column]:
                        i1= row
                        j1 = column

                    if str[1] == matrix[row][column]:
                        i2= row
                        j2 = column

            if i1 == i2 :
                if j1 == 0:
                    j1= 5
                if j2 == 0:
                    j2 = 5
                pt[letter]= matrix[i1][j1-1]+matrix[i1][j2-1]
            elif j1 == j2 :
                if i1 == 0:
                    i1 = 5
                if i2 == 0:
                    i2 = 5
                pt[letter]= matrix[i1-1][j1]+matrix[i2-1][j1]
            else:
                pt[letter]= matrix[i1][j2]+matrix[i2][j1]

        plaintext = ''.join(pt)
        for letter in range(len(plaintext)-1):
            if plaintext[letter] == 'x':
                plaintext = plaintext[:letter]+plaintext[letter+1:len(plaintext)]
        if plaintext[len(plaintext)-1] == 'x':
            plaintext= plaintext[:len(plaintext)-1]

        return plaintext

    def encrypt(self, plainText: str, key:str ) -> str:
        #raise NotImplementedError

        checked = {}
        alphabet = "abcdefghiklmnopqrstuvwxyz"
        for i in range(25):
            checked[alphabet[i]]= False

        matrix = [[0 for row in range(5)] for column in range(5) ]
        db = key.lower() + alphabet.lower()
        plaintext = plainText.lower()


        row = 0
        column = 0
        for letter in db:
            if row < 5 and column < 5:
                if checked[letter] is False and letter != 'j':
                    matrix[row][column] = letter
                    checked[letter] = True
                    column = column +1
                elif letter == 'j' and checked['i'] is False:
                    matrix[row][column] = 'i'
                    checked['i'] = True
                    column = column


                if column == 5:
                    row = row+1
                    column = 0

        length = len(plaintext)
        for letter in range(length-1):
            if plaintext[letter] == plaintext[letter+1]:
                plaintext = plaintext[:letter+1]+'x'+plaintext[letter+1:length]

        if len(plaintext)%2 != 0 :
            plaintext = plaintext + 'x'

        length = len(plaintext)/2
        pt=["" for letter in range(length)]
        ct=["" for letter in range(length)]


        count = 0
        for i in range(length):
            pt[i]=plaintext[count] + plaintext[count+1]
            count = count+2

        for letter in range(length):
            str = pt[letter]
            for row in range(5):
                for column in range(5):
                    if str[0] == matrix[row][column]:
                        i1= row
                        j1 = column

                    if str[1] == matrix[row][column]:
                        i2= row
                        j2 = column

            if i1 == i2 :
                if j1 == 4:
                    j1= -1
                if j2 == 4:
                    j2 = -1
                ct[letter]= matrix[i1][j1+1]+matrix[i1][j2+1]
            elif j1 == j2 :
                if i1 == 4:
                    i1 = -1
                if i2 == 4:
                    i2 = -1
                ct[letter]= matrix[i1+1][j1]+matrix[i2+1][j1]
            else:
                ct[letter]= matrix[i1][j2]+matrix[i2][j1]

        cipher = ''.join(ct)

        return cipher
