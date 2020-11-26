from analisador_lexico.LerArquivoEntrada import LerArquivo
from analisador_lexico.Token import Token
from analisador_lexico.TipoToken import TipoToken
import string

tokens = {
    '(': Token(TipoToken.AbrePar, '('),
    ')': Token(TipoToken.FechaPar, ')'),
    '<>': Token(TipoToken.OpRelDif, '<>'),
    '>': Token(TipoToken.OpRelMaior, '>'),
    '>=': Token(TipoToken.OpRelMaiorIgual, '>='),
    '<': Token(TipoToken.OpRelMenor, '<'),
    '<=': Token(TipoToken.OpRelMenorIgual, '<='),
    '=': Token(TipoToken.OpRelIgual, '='),
}

TIPOS_OPERADORES_ARITIMETICOS = {
    '*': TipoToken.OpAritMult,
    '/': TipoToken.OpAritDiv,
    '+': TipoToken.OpAritSoma,
    '-': TipoToken.OpAritSub,
}

TIPOS_PALAVRAS_CHAVES = {
    'DECLARACOES': TipoToken.PCDeclaracoes,
    'ALGORITMO': TipoToken.PCAlgoritmo,
    'INT': TipoToken.PCInteiro,
    'REAL': TipoToken.PCReal,
    'ATRIBUIR': TipoToken.PCAtribuir,
    'A': TipoToken.PCA,
    'LER': TipoToken.PCLer,
    'IMPRIMIR': TipoToken.PCImprimir,
    'SE': TipoToken.PCSe,
    'ENTAO': TipoToken.PCEntao,
    'ENQUANTO': TipoToken.PCEnquanto,
    'INICIO': TipoToken.PCInicio,
    'FIM': TipoToken.PCFim,
    'E': TipoToken.OpBoolE,
    'OU': TipoToken.OpBoolOu,
}

operators = ['<', '>', '=', 'A', 'E']


class Analisador:
    def __init__(self, nome_arquivo: str):
        self.leitor = LerArquivo(nome_arquivo)

    def ler_proximo_token(self) -> Token:
        self.ignorar_espacos_comentarios()
        self.leitor.confirmar()

        # print('Verifica fim')
        if token := self.fim():
            self.leitor.confirmar()
            return token
        else:
            self.leitor.zerar()

        # print('Verifica palavra chave')
        if token := self.palavras_chaves():
            self.leitor.confirmar()
            return token
        else:
            self.leitor.zerar()

        # print('Verifica variavel')
        if token := self.variavel():
            self.leitor.confirmar()
            return token
        else:
            self.leitor.zerar()

        # print('Verifica numero')
        if token := self.numeros():
            self.leitor.confirmar()
            return token
        else:
            self.leitor.zerar()

        # print('Verifica operador aritimetico')
        if token := self.operadores_aritimeticos():
            self.leitor.confirmar()
            return token
        else:
            self.leitor.zerar()

        # print('Verifica operador relacional')
        if token := self.operador_relacional(): 
            self.leitor.confirmar()
            return token
        else:
            self.leitor.zerar()

        # print('Verifica delimitador')
        if token := self.delimitador():
            self.leitor.confirmar()
            return token
        else:
            self.leitor.zerar()

        # print('Verifica parenteses')
        if token := self.parenteses():
            self.leitor.confirmar()
            return token
        else:
            self.leitor.zerar()

        # print('Verifica cadeia')
        if token := self.cadeia():
            self.leitor.confirmar()
            return token
        else:
            self.leitor.zerar()

        # print("\n\nErro léxico")
        print(self.leitor.lexema)
        raise SystemExit

    def fim(self):
        c = self.leitor.lerProximoChar()

        if c == '':
            return Token(TipoToken.Fim, "FIM")
        self.leitor.retroceder()
        return None

    def cadeia(self):
        c = self.leitor.lerProximoChar()

        if c == '\'':
            while True:
                c = self.leitor.lerProximoChar()

                if c == '\'':
                    return Token(TipoToken.Cadeia, self.leitor.lexema)
                elif c == '':
                    print('\nCadeia de caracteres não foi fechada')
                    raise SystemExit
        else:
            return None

    def parenteses(self):
        c = self.leitor.lerProximoChar()
        if c == '(':
            return Token(TipoToken.AbrePar, self.leitor.lexema)
        elif c == ')':
            return Token(TipoToken.FechaPar, self.leitor.lexema)
        return None

    def delimitador(self):
        c = self.leitor.lerProximoChar()
        if c == ':':
            return Token(TipoToken.Delim, self.leitor.lexema)
        return None

    def operador_relacional(self):
        c = self.leitor.lerProximoChar()

        if c == '<':
            c = self.leitor.lerProximoChar()
            if c == '>':
                return Token(TipoToken.OpRelDif, self.leitor.lexema)
            elif '=':
                return Token(TipoToken.OpRelMenorIgual, self.leitor.lexema)
            else:
                self.leitor.retroceder()
                return Token(TipoToken.OpRelMenor, self.leitor.lexema)
        elif c == '=':
            return Token(TipoToken.OpRelIgual, self.leitor.lexema)
        elif c == '>':
            c = self.leitor.lerProximoChar()
            if c == '=':
                return Token(TipoToken.OpRelMaiorIgual, self.leitor.lexema)
            else:
                self.leitor.retroceder()
                return Token(TipoToken.OpRelMaior, self.leitor.lexema)
        else:
            return None

    def operadores_aritimeticos(self):
        c = self.leitor.lerProximoChar()
        lexema = self.leitor.lexema

        if tipo := TIPOS_OPERADORES_ARITIMETICOS.get(lexema, False) :
            print(tipo)
            return Token(tipo, lexema)
        return None

    def numeros(self):
        c = self.leitor.lerProximoChar()
        # 243
        # +/-242
        # 234.123

        if c == '+' or c == '-' or c.isdigit():
            flag = False
            if c == '+' or c == '-':
                self.leitor.lerProximoChar()
            while True:
                c = self.leitor.lerProximoChar()
                if c.isdigit():
                    continue
                # Recebe um ponto e verifica se o próximo caractere é um número
                elif c == '.':
                    c = self.leitor.lerProximoChar()
                    # Se o caractere após a virgula não for um número retorne None
                    if not c.isdigit():
                        return None
                else:
                    self.leitor.retroceder()
                    break

            lexema = self.leitor.lexema
            if flag:
                return Token(TipoToken.NumReal, lexema)
            else:
                return Token(TipoToken.NumInt, lexema)

        else:
            return None

    def variavel(self):
        c = self.leitor.lerProximoChar()
        if c != '' and c in string.ascii_lowercase:
            while str.isalnum(c):
                c = self.leitor.lerProximoChar()
            self.leitor.retroceder()
            lexema = self.leitor.lexema
            return Token(TipoToken.Var, lexema)
        else:
            return None

    def palavras_chaves(self):
        while True:
            c = self.leitor.lerProximoChar()
            if c == '' or c not in string.ascii_uppercase:
                self.leitor.retroceder()
                lexema = self.leitor.lexema.strip()
                # print('|' + lexema + '|')
                # Tenta buscar o tipo token, no dicionário
                # caso não encontrar irá retornar None que será retornado
                if tipo_token := TIPOS_PALAVRAS_CHAVES.get(lexema, None):
                    return Token(tipo_token, lexema)
                else:
                    return None

    def fim(self):
        c = self.leitor.lerProximoChar()

        if c == '':
            return Token(TipoToken.Fim, "FIM")
        return None

    def ignorar_espacos_comentarios(self):
        char = self.leitor.lerProximoChar()
        while char in ['\n', ' ', '%']:
            if char == '%':
                while char != '\n':
                    char = self.leitor.lerProximoChar()
            char = self.leitor.lerProximoChar()
        self.leitor.retroceder()
