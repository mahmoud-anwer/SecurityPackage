

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
        raise NotImplementedError

    def encrypt(self, plainText: str, key:str ) -> str:
        raise NotImplementedError
