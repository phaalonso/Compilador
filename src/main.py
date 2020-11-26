#!/usr/bin/python3
import sys

import analisador_lexico.Analisador as Lexico

# Evitar esse código ser executado durante importação
if __name__ == "__main__":
    print(sys.argv[1])
    analisador = Lexico.Analisador(sys.argv[1])

    t = analisador.ler_proximo_token()
    while t.token != Lexico.TipoToken.Fim :
        t = analisador.ler_proximo_token()
        print(t, end='\n')


