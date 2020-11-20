import enum

class TipoToken(enum.Enum):
    PCDeclaracoes = 0
    PCAlgoritmo = 1
    PCAtribuir = 2
    PCInteiro = 3
    PCReal = 4
    PCA = 5
    PCLer = 6
    PCImprimir = 7
    PCSe = 8
    PCEntao = 9
    PCEnquanto = 10
    PCInicio = 11
    PCFim = 12
    OpAritMult = 13
    OpAritDiv = 14
    OpAritSoma = 15
    OpAritSub = 16
    OpRelMenor = 17
    OpRelMenorIgual = 18
    OpRelMaiorIgual  = 19
    OpRelMaior = 20
    OpRelIgual = 21
    OpRelDif  = 22
    OpBoolE = 23
    OpBoolOu  = 24
    Delim = 25
    AbrePar = 26
    FechaPar = 27
    Var = 28
    NumInt = 29
    NumReal = 30
    Cadeia = 31
    Fim = 32
