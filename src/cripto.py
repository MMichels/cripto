from cryptography.fernet import Fernet


class Cripto:
    def __init__(self, key: bytes):
        self.cripto = Fernet(key)

    def criptografar(self, texto: str):
        texto = self.cripto.encrypt(bytes(texto.encode('utf-8')))
        return str(texto)[2:-1]

    def descriptografar(self, texto: str):
        texto = self.cripto.decrypt(bytes(texto.encode('utf-8')))
        return str(texto)[2:-1]

    @staticmethod
    def gerar_chave():
        return Fernet.generate_key()
