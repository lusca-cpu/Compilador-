from sintatico import Sintatico
from tabela import Tabela

if __name__ == '__main__':

    print('Para imprimir a tabela de simbolos digite -t antes de digitar o exemplo (ex: -t exemplo1.txt).')
    nome = input("Digite o nome do arquivo (ex: exemplo1.txt): ")
    tabSim = Tabela()
    tab = None
    aux = 0
    
    if (nome[0] == '-' and (nome[1] == 't')):
        aux = 1
        nome = nome[3:]
           
    compilador = Sintatico()
    ok = compilador.interprete('exemplos/' + nome)
    tab = compilador.chamaTabela()

    if aux == 1:
        tab.printtabela(nome)
    
    if ok:
        print('COMPILADO COM SUCESSO.')

