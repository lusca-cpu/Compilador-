class Token:
    def __init__(self, tipo, lexema, linha):
        self.tipo = tipo
        (cosnt, msg) = tipo
        self.const = cosnt
        self.msg = msg 
        self.lexema = lexema
        self.linha = linha 
