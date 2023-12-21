from tipo_token import TipoToken 
from token_1 import Token
from os import path

class Lexico:
    reservadas = {'programa': TipoToken.PROGRAMA, 'variaveis': TipoToken.VARIAVEIS, 'inteiro': TipoToken.INTEIRO, 'real': TipoToken.REAL, 'logico': TipoToken.LOGICO, 
                  'caracter': TipoToken.CARACTER, 'se': TipoToken.SE, 'senao': TipoToken.SENAO, 'enquanto': TipoToken.ENQUANTO, 'leia': TipoToken.LEIA, 
                  'escreva': TipoToken.ESCREVA, 'falso': TipoToken.FALSO, 'verdadeiro': TipoToken.VERDADEIRO} 

    def __init__ (self, nomeArquivo):
        self.nomeArquivo = nomeArquivo
        self.arquivo = None

    def abrirArquivo(self): 
        if not self.arquivo is None:
            print("Erro, arquivo ja aberto.")
            quit()
        elif path.exists(self.nomeArquivo):
            self.arquivo = open(self.nomeArquivo, "r")
            self.buffer = ''
            self.linha = 1
        else:
            print(f'Erro, arquivo {self.nomeArquivo} não existe.')
            quit()

    def fechaArquivo(self):
        if self.arquivo is None:
            print('Erro, não tem arquivo aberto.')
            quit()
        else:
            self.arquivo.close()

    def getChar(self):
        if self.arquivo is None:
            print('Erro, não tem arquivo aberto.')
            quit()
        elif len(self.buffer) > 0:
            c = self.buffer[0]
            self.buffer = self.buffer[1:]
            return c
        else:
            c = self.arquivo.read(1)

            if len(c)==0:
                return None
            else: 
                return c.lower()

    def ungetChar(self, c):
        if not (c is None) and (c != '*'):
            self.buffer = self.buffer + c 

    def getToken(self):
        lexema = ''
        estado = 1
        car = None
        while (True):
            if estado == 1:
                car = self.getChar()

                if car is None:
                    return Token(TipoToken.FIMARQ, '<eof>', self.linha)
                elif car in {' ', '\t', '\n'}:
                    if car == '\n':
                        self.linha = self.linha + 1
                elif car.isalpha():
                    # ESTADO PARA TRATAR NOME 
                    estado = 2
                elif car.isdigit():
                    # ESTADO PARA TRATAR NÚMEROS 
                    estado = 3
                elif car in {'"', '=', '<', '>', '+', '-', '*', '/', '!', ';', ':', ',', '(', ')', '{', '}', '.'}:
                    # ESTADO PARA TRATAR OS TOKENS PRIMITIVOS
                    estado = 4
                else :
                    return Token(TipoToken.ERRO, '<' + car + '>', self.linha)
                
            elif estado == 2:
                # ESTADO PARA TRATAR NOME 
                lexema += car
                car = self.getChar()
                
                if car is None or (not car.isalnum()):
                    self.ungetChar(car) 
                    if lexema in Lexico.reservadas:
                        return Token(Lexico.reservadas[lexema], lexema, self.linha)
                    else:
                        if len(lexema) < 17: #CONFERINDO SE O IDENTIFICADOR TEM 16 CARACTERES
                            return Token(TipoToken.IDENT, lexema, self.linha)
                        else:
                            return Token(TipoToken.ERRO, '<' + lexema + '>', self.linha)
            
            elif estado == 3:
                # ESTADO PARA TRATAR NÚMEROS
                lexema += car
                car = self.getChar()

                if car == '.':
                    lexema += car
                    car = self.getChar()
                
                elif car is None or (not car.isdigit()):
                    self.ungetChar(car)
                    if lexema.count(".") > 1:
                            print(f'ERRO LÉXICO NA LINHA {self.linha}!')
                            quit()
                    elif lexema.isdigit():
                        # RETORNANDO UM NÚMERO REAL
                        return Token(TipoToken.CTE, lexema, self.linha)
                    else:
                        # RETORNANDO UM NÚMERO INTEIRO
                        return Token(TipoToken.CTE, lexema, self.linha)
            
            elif estado == 4:
                # ESTADO PARA TRATAR OS TOKENS PRIMITIVOS
                lexema += car
                if car == '=':
                    return Token(TipoToken.OPRELD, lexema, self.linha)
                elif car == '<':
                    aux = self.getChar()
                    if aux == '=':
                        lexema = car + aux
                        return Token(TipoToken.OPRELD, lexema, self.linha)
                    elif aux == '>':
                        lexema = car + aux
                        return Token(TipoToken.OPRELD, lexema, self.linha)
                    else:
                        return Token(TipoToken.OPRELD, lexema, self.linha)
                elif car == '>':
                    aux = self.getChar()
                    if aux == '=':
                        lexema = car + aux
                        return Token(TipoToken.OPRELD, lexema, self.linha)
                    else:
                        return Token(TipoToken.OPRELD, lexema, self.linha)
                elif car in {'+', '-'}: 
                    return Token(TipoToken.OPAD, lexema, self.linha)
                elif car == '*':
                    return Token(TipoToken.OPMUL, lexema, self.linha)
                elif car == '/':
                    aux = self.getChar()
                    if aux == '/':
                        estado = 5
                    elif aux == '*':
                        estado = 5
                    else:
                        return Token(TipoToken.OPMUL, lexema, self.linha)
                elif car == '!':
                    return Token(TipoToken.OPNEG, lexema, self.linha)
                elif car == ';':
                    return Token(TipoToken.PVIRG, lexema, self.linha)
                elif car == ':':
                    aux = self.getChar()
                    if aux == '=':
                        lexema = car + aux
                        return Token(TipoToken.ATRIB, lexema, self.linha)
                    else:
                        return Token(TipoToken.DPONTOS, lexema, self.linha)
                elif car == ',':
                    return Token(TipoToken.VIRG, lexema, self.linha)
                elif car == '(':
                    return Token(TipoToken.ABREPAR, lexema, self.linha)
                elif car == ')':
                    return Token(TipoToken.FECHAPAR, lexema, self.linha)
                elif car == '{':
                    return Token(TipoToken.ABRECH, lexema, self.linha)
                elif car == '}':
                    return Token(TipoToken.FECHACH, lexema, self.linha)
                elif car == '"':
                    car = self.getChar()
                    lexema += car
                    while car != '"':
                        car = self.getChar()
                        if car is not None:
                            lexema += car
                        else:
                            print(f'ERRO LÉXICO NA LINHA {self.linha}!')
                            quit()
                    return Token(TipoToken.CADEIA, lexema[1:-1], self.linha)

            elif estado == 5:
                # CONSUMINDO COMENTARIO
                if aux == '/':
                    while (not car is None) and (car != '\n'):
                        car = self.getChar()                    
                else: 
                    while (not car is None):
                        car = self.getChar()
                        if car == '*':
                            aux = self.getChar()
                            if aux == '/':
                                break
                        elif car == None:
                            print(f'ERRO LÉXICO NA LINHA {self.linha}!')
                            quit()
                self.ungetChar(car)
                lexema = '' 
                estado = 1
