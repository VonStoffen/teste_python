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

    def adicionar_pessoa(self, nome: str, idade: int, altura: float, peso: float) -> None:
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        pessoa = dict(nome=nome, idade=idade, altura=altura, peso=peso)
        self.lista_pessoas.append(pessoa)

    def listar_pessoas(self) -> None:
        for item in self.lista_pessoas:
            print(item['nome'], item['idade'], item['altura'],item['peso'])
    
    def achar_pessoa(self, nome) -> None:
        for i, item in enumerate(self.lista_pessoas):
            if item['nome'] == nome:
                print(f'Achado {nome} na posição {i}')
                break
        else:
            print(f'{nome} não achado na lista')
    def listar_nome_peso(self):
        for item in self.lista_pessoas:
            print("Nome: ",item['nome'],"Peso: ",item['peso'])

    def trocar_idade(self, nome, idade):
        for item in self.lista_pessoas:
            if item['nome'] == nome:
                item['idade'] = idade
                print('Idade alterada com sucesso...')
                print(item['nome'], 'Nova idade', item['idade'])
                break
        else:
            print(f'{nome} não achado na lista')

    def retirar_pessoas(self, nome):
        for item in(self.lista_pessoas):
            if item['nome'] == nome:
                self.lista_pessoas.remove(item)
                print(f'Registro da pessoa {nome} removido com sucesso...')
                #print(item['nome'], item['idade'])
                break
        else:
            print(f'{nome} não achado na lista')
    def ordenar_idade(self, ordem: bool=False):
        '''Órdem True e ordem Descendente e False e Ascendente'''
        for item in(self.lista_pessoas):
            idade = item['idade']
            pessoas_ordenada = sorted(idade,reverse=ordem)
            print(pessoas_ordenadas)



            

    