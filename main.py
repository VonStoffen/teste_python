import modules.pessoas as mp

def main():
    pessoa = mp.Pessoa()
    
    while True:
        print("\nMenu:")
        print("1 - Adicionar pessoa")
        print("2 - Listar pessoas")
        print("3 - Procurar pessoa")
        print("4 - Salvar")
        print("5 - Carregar")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            altura = float(input("Altura: "))
            peso = float(input("Peso: "))
            try:
                pessoa.validar_pessoa(nome, idade, altura, peso)
                pessoa.adicionar_pessoa(nome, idade, altura, peso)
                print(f'Pessoa {nome} adicionada com sucesso!')
            except ValueError as e:
                print(f'Erro: {e}')
        
        elif opcao == '2':
            pessoa.listar_pessoas()
        
        elif opcao == '3':
            nome = input("Nome da pessoa a procurar: ")
            pessoa.achar_pessoa(nome)
        
        elif opcao == '4':
            caminho = input("Caminho do arquivo para salvar: ")
            pessoa.salvar_em_arquivo(caminho)
            print(f'Lista de pessoas salva em {caminho}')
        
        elif opcao == '5':
            caminho = input("Caminho do arquivo para carregar: ")
            try:
                pessoa.carregar_de_arquivo(caminho)
                print(f'Lista de pessoas carregada de {caminho}')
            except FileNotFoundError:
                print(f'Arquivo {caminho} não encontrado.')
        
        elif opcao == '0':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")
    
if __name__ == '__main__':
    main()