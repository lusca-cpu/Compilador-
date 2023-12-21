class Tabela:
    def __init__(self):
        self.tabela = {}
        self.arqv = None

    def existeIdent(self, nome):
        if nome in self.tabela:
            return True
        else:
            return False
        
    def declaraIdent(self, nome, valor):
        if not self.existeIdent(nome):
            self.tabela[nome] = valor
            return True
        else:
            return False
        
    def pegaValor(self, nome):
        return self.tabela[nome]

    def atribuiValor(self, nome, valor):
        self.tabela[nome] = valor

    def printtabela(self, arquivo):
        self.arqv = open(arquivo, 'w')
        self.arqv.write(str(self.tabela))
        self.arqv.close()   