import json
from dataclasses import asdict
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

    def validar_pessoa(self, nome: str, idade: float, altura: float, peso: float) -> bool:
        #Dispare erros apropriados (ValueError) com mensagens claras:
        if idade < 0 or altura < 0 or peso < 0:
            raise ValueError('Idade, altura e peso não podem ser negativos')
        if not nome:
            raise ValueError('Nome não pode ser vazio')
        return True
    
    def salvar_em_arquivo(self, nome_arquivo: str) -> None:
            try:
                with open(nome_arquivo, 'x') as arquivo:
                    json.dump(self.lista_pessoas, arquivo, indent=4)
            except Exception as e:
                print(f'Erro ao salvar arquivo: {e}')

    def carregar_de_arquivo(self, nome_arquivo: str) -> None:
            with open(nome_arquivo, 'r') as arquivo:
                self.lista_pessoas = json.load(arquivo)]

    def listar_pessoas_ordenadas_por_idade(self) -> None:
        pessoas_ordenadas = sorted(self.lista_pessoas, key=lambda x: x['idade'])
        print(f'Pessoas ordenadas por idade: {pessoas_ordenadas}')
    def filtrar_pessoas_por_idade(self, idade_minima: int) -> None:
        pessoas_filtradas = [pessoa for pessoa in self.lista_pessoas if pessoa['idade'] > idade_minima]
        print(f'Pessoas com idade maior que {idade_minima}: {pessoas_filtradas}')