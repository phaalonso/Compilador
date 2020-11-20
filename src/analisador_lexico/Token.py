from analisador_lexico.TipoToken import TipoToken

class Token:
    def __init__(self, token = None, lexema = None):
        self.token: TipoToken = token
        self.lexema: str = lexema

    def __str__(self):
        return '<{}, {}>'.format(self.token.name, self.lexema)
