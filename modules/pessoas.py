'''
1 - Criar uma classe chamada: Pessoa
    1.1 - Precisa ter uma caracteristicas: Peso, Altura, Nome, Idade
* Ter a classe pessoa para criar uma lista de pessoas usando a classe
'''

class Pessoa:
    
    def __init__(self) -> None:
        self.nome: str = ''
        self.idade: int = 0
        self.altura: float = 0.
        self.peso: float = 0.
        self.lista_pessoas = []
          
    # nome: str = ''
    # idade: int = 0
    # altura: float = 0.
    # peso: float = 0.
    # lista_pessoas = []

    def adicionar_pessoa(self, nome: str, idade: int, altura: float, peso: float) -> None:
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        pessoa = dict(nome=nome, idade=idade, altura=altura, peso=peso)
        self.lista_pessoas.append(pessoa)

    def listar_pessoas(self) -> None:
        print(f'{self.lista_pessoas}')

    def __str__(self) -> str:
       return f'{self.nome}, {self.idade}, {self.altura}, {self.peso}'
    
    def achar_pessoa(self, nome) -> None:
        for i, item in enumerate(self.lista_pessoas):
            if item['nome'] == nome:
                print(f'Achado {nome} na posição {i}')
                break
        else:
            print(f'{nome} não achado na lista')