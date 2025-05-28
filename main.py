import modules.pessoas as mp


def main():
    p1 = mp.Pessoa()
    p1.adicionar_pessoa('Rodrigo', 18,1.70,65)
    p2 = mp.Pessoa()
    p2.adicionar_pessoa('Damião', 26,1.80,78)
    #print(p1)
    #print(p2)
    #p2.listar_pessoas()
    p2.adicionar_pessoa('Victor', 27, 1.67, 85)
    p1.listar_pessoas()
    p2.listar_pessoas()
    

    p2.achar_pessoa('Victor')
    
if __name__ == '__main__':
    main()