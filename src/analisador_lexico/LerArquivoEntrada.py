import sys

class LerArquivo:
    def __init__(self, nome):
        try:
            self.file = open(nome, 'r')
        except FileNotFoundError:
            print("Arquivo não encontrado")
            raise SystemExit(-1)

    def ler_caractere(self) -> str:
        return self.file.read(1)

    def seek(self, n: int):
        self.file.seek(n)

    def tell(self) -> int:
        return self.file.tell()

    def __del__(self):
        try:
            if self.file != None:
                self.file.close()
        except AttributeError:
            # Ocorre quando uma exceção é lançada no try catch presente no construtor.
            # o que faz que ele tente usar esse destrutor, mas devido a exceção o atributo self.file não foi definido
            pass