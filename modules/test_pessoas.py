import unittest
import json
from modules.pessoas import Pessoa

class TestPessoa(unittest.TestCase):
    def setUp(self):
        self.pessoa = Pessoa()
        self.pessoa.adicionar_pessoa("João", 30, 1.75, 70.0)
        self.pessoa.adicionar_pessoa("Maria", 25, 1.65, 60.0)

    def test_adicionar_pessoa_valida(self):
        self.pessoa.adicionar_pessoa("Carlos", 40, 1.80, 80.0)
        self.assertEqual(len(self.pessoa.lista_pessoas), 3)

    def test_adicionar_pessoa_invalida(self):
        with self.assertRaises(ValueError):
            self.pessoa.validar_pessoa("", -5, -1.75, -70.0)

    def test_achar_pessoa(self):
        self.assertIsNone(self.pessoa.achar_pessoa("João"))
        self.assertIsNone(self.pessoa.achar_pessoa("Ana"))

    def test_salvar_em_arquivo(self):
        caminho = "test_pessoas.json"
        self.pessoa.salvar_em_arquivo(caminho)
        with open(caminho, 'r') as arquivo:
            data = json.load(arquivo)
            self.assertEqual(len(data), 2)

    def test_carregar_de_arquivo(self):
        caminho = "test_pessoas.json"
        self.pessoa.salvar_em_arquivo(caminho)
        nova_pessoa = Pessoa()
        nova_pessoa.carregar_de_arquivo(caminho)
        self.assertEqual(len(nova_pessoa.lista_pessoas), 2)