import sys
from typing import List

class LerArquivo:
    tamanho_buffer = 20

    def __init__(self, nome_arquivo: str):
        try:
            self.file = open(nome_arquivo, 'r')
            self.buffer: List[str] = [None] * LerArquivo.tamanho_buffer * 2
            self.ponteiro = 0
            self.inicioLexema = 0
            self.__lexema = []
            self.bufferAtual = '2'
            self.recarregarBufferEsquerda()
        except FileNotFoundError:
            print("Arquivo não encontrado")
            raise SystemExit(-1)

    @property
    def lexema(self):
        return ''.join(self.__lexema)

    def lerCaractereBuffer(self) -> str:
        """
            Método utilizado para ler um caractere do buffer de leitura
        """
        char = self.buffer[self.ponteiro]
        self.incrementarPonteiro()
        return char

    def lerProximoChar(self):
        char = self.lerCaractereBuffer()
        self.__lexema.append(char)
        # print('Ler proximo: ' + char )
        return char

    def retroceder(self):
        """
            Retrocede uma posição no buffer
            - Se chegar em uma posição menor que zero, aponta para a ultima posição
        """
        self.ponteiro -= 1
        self.__lexema.pop()
        if self.ponteiro < 0:
            self.ponteiro = self.tamanho_buffer * 2 -1

    def incrementarPonteiro(self):
        """
            Método usado para incrementação do ponteiro, caso ele chegue no começo
            do buffer direito (self.tamanho_buffer) irá carregalo, e quando chegar no final
            irá carregar o lado esquerdo do buffer e mover seu ponteiro para ele
        """
        self.ponteiro += 1
        if self.ponteiro == self.tamanho_buffer:
            self.recarregarBufferDireita()
        elif self.ponteiro == self.tamanho_buffer * 2:
            self.recarregarBufferEsquerda()
            self.ponteiro = 0
            
    def recarregarBufferEsquerda(self):
        """
            Recarrega o lado esquerdo do buffer
            - 0 até self.tamanho_buffer
        """
        if self.bufferAtual == '2':
            self.bufferAtual = '1'
            for i in range(0, self.tamanho_buffer):
                self.buffer[i] = self.file.read(1)

    def recarregarBufferDireita(self):
        """
            Recarrega o lado esquerdo do buffer
            - self.tamanho_buffer até self.tamanho_buffer * 2
        """
        if self.bufferAtual == '1':
            self.bufferAtual = '2'
            for i in range(self.tamanho_buffer, self.tamanho_buffer * 2):
                self.buffer[i] = self.file.read(1)

    def confirmar(self):
        self.inicioLexema = self.ponteiro
        self.__lexema = []
    
    def zerar(self):
        self.ponteiro = self.inicioLexema
        self.__lexema = []

    def __del__(self):
        try:
            if self.file != None:
                self.file.close()
        except AttributeError:
            # Ocorre quando uma exceção é lançada no try catch presente no construtor.
            # o que faz que ele tente usar esse destrutor, mas devido a exceção o atributo self.file não foi definido
            print('Fechando o buffer')
            pass