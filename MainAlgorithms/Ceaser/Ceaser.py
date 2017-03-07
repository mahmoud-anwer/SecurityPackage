

class Ceaser:
    def encrypt(self, plainText: str, key: int) -> str:
        # raise NotImplementedError
        encrypted_text = ""
        for _char in plainText:
            ascii_char = ord(_char) + key
            if ascii_char > ord('z'):
                ascii_char = ascii_char - ord('z') + ord('a') - 1
            encrypted_text += chr(ascii_char)

        return encrypted_text.upper()

    def decrypt(self, cipherText: str, key: int) -> str:
        # raise NotImplementedError
        plain_text = ""
        for _char in cipherText:
            ascii_char = ord(_char) - key
            if ascii_char < ord('a'):
                ascii_char = ord('z') - (ord('a') - ascii_char)
            plain_text += chr(ascii_char)

        return plain_text.upper()

    def analyse(self, plainText: str, cipher: str) -> int:
        # raise NotImplementedError
        plainText = plainText.lower()
        cipher = cipher.lower()
        key = ord(cipher[0]) - ord(plainText[0])
        if key > ord('z'):
            key = key - ord('z')
        return key
