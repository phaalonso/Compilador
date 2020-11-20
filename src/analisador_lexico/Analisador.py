from analisador_lexico.LerArquivoEntrada import LerArquivo
from analisador_lexico.Token import Token
from analisador_lexico.TipoToken import TipoToken

tokens = {
    ':': Token(TipoToken.Delim, ':'),
    '*': Token(TipoToken.OpAritMult, '*'),
    '/': Token(TipoToken.OpAritDiv, '/'),
    '+': Token(TipoToken.OpAritSoma, '+'),
    '-': Token(TipoToken.OpAritSub, '-'),
    '(': Token(TipoToken.AbrePar, '('),
    ')': Token(TipoToken.FechaPar, ')'),
    '<>': Token(TipoToken.OpRelDif, '<>'),
    '>': Token(TipoToken.OpRelMaior, '>'),
    '>=': Token(TipoToken.OpRelMaiorIgual, '>='),
    '<': Token(TipoToken.OpRelMenor, '<'),
    '<=': Token(TipoToken.OpRelMenorIgual, '<='),
    '=': Token(TipoToken.OpRelIgual, '=')
}

operators = ['<', '>', '=']


class Analisador:
    def __init__(self, nome_arquivo: str):
        self.arquivo = LerArquivo(nome_arquivo)

    def ler_token(self) -> Token:
        texto = []

        while caractere := self.arquivo.ler_caractere():
            # Se for um caractere especial, e ainda não possuir nenhuk
            # caractere armazenado, ele irá ignorar
            if caractere in [' ', '', '\n', '\r', '\t']:
                # Caso possui caractere armazendos ele sai do loop, senão ele
                # continua procurando os caracteres
                if len(texto) > 0:
                    break
                pass
            else:
                # Se for algum simbolo indicando uma operação, ele espera a leitura
                # antes de poder sair. Para poder verificar caracteres de operação
                # com mais de um dígito
                # print(texto, caractere)
                if caractere not in operators:
                    if aux := tokens.get(caractere):
                        # Se o caractere atual for um lexema, e tiver texto deverá apontar
                        # o ponteiro, um caractere para trás
                        # assim ele sairá do loop retornara o texto,
                        # e voltar para essa função fazendo que o lexema será processado
                        if len(texto) > 0:
                            self.arquivo.seek(self.arquivo.tell() - 1)
                            break
                        else:
                            return aux
                else:
                    #! Caractere é um operador como <, >, =
                    # Verifica se o buffer possui algum caracteres, se possuir e ele não for um dos lexemas irá retornar um caractere para trás
                # any(char in operators for char in texto) => verifica se alguns dos caracteres presentes em texto é um dos operadores
                    if len(texto) > 0:
                        if not any(char in operators for char in texto):
                            self.arquivo.seek(self.arquivo.tell() - 1)
                            break
                        else:
                            # print('Eae kkk', texto, caractere)
                            texto.append(caractere)
                            break

                texto.append(caractere)
                # print(texto)

        # Retorna o Token processado, caso não encontrá-lo irá
        # retornar o próprio texto
        formed_str = ''.join(texto)
        return tokens.get(formed_str, formed_str)
