#!/usr/bin/python3
import sys

import analisador_lexico.Analisador as Lexico

# Evitar esse código ser executado durante importação
if __name__ == "__main__":
    print(sys.argv[1])
    analisador = Lexico.Analisador(sys.argv[1])

    while t := analisador.ler_token():
        print(t, end='\n')


