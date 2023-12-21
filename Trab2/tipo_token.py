class TipoToken:
    # PALAVRAS RESERVAVDAS 
    PROGRAMA = (1, 'programa')
    VARIAVEIS = (2, 'variaveis')
    
    # TIPOS BASICO DA LINGUAGEM
    INTEIRO = (3, 'inteiro')
    REAL = (4, 'real')
    LOGICO = (5, 'logico')
    CARACTER = (6, 'caracter')

    # PALAVRAS RESERVAVDAS
    SE = (7, 'se')
    SENAO = (8, 'senao')
    ENQUANTO = (9, 'enquanto')
    LEIA = (10, 'leia')
    ESCREVA = (11, 'escreva')
    FALSO = (12, 'falso')
    VERDADEIRO = (13, 'verdadeiro')

    # TOKEN PRIMITIVOS
    ATRIB = (14, ':=')
    OPRELD = (15, '=, <, >, <=, >=, <>')
    OPAD = (16, '+, -')
    OPMUL = (17, '*, /')
    OPNEG = (18, '!')
    PVIRG = (19, ';')
    DPONTOS = (20, ':')
    VIRG = (21, ',')
    ABREPAR = (22, '(')
    FECHAPAR = (23, ')')
    ABRECH = (24, '{')
    FECHACH = (25, '}')
    PONTO = (26, '.')
    
    IDENT = (27, 'ident')
    ERRO = (28, 'erro')
    FIMARQ = (29, 'eof')
    CADEIA = (30, 'cadeia')

    # NÚMEROS 
    CTE = (31, 'cte')
