import modules.pessoas as mp

def main():
    p1 = mp.Pessoa()
    p1.adicionar_pessoa('José', 2,.70,11)
    p1.adicionar_pessoa('Maria', 1,.50,5)
    p1.adicionar_pessoa('Victor', 27, 1.67, 85)
    p1.listar_pessoas()
    #p1.achar_pessoa('José')
    #p1.achar_pessoa('Maria')
    #p1.achar_pessoa('Victor')
    #p1.listar_nome_peso()
    #p1.trocar_idade('Maria', 2)
    #p1.listar_pessoas()
    #p1.retirar_pessoas('Victor')
    #p1.listar_pessoas()
    p1.ordenar_idade(1)

if __name__ == '__main__':
    main()