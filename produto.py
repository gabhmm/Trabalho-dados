
from pilha import Pilha

pilhaproduto = Pilha()

class Produto:
    def __init__(self):
        self.ID = 100
        self.nome = None
        self.quantidade = None
        self.preco = None

    def cadastrar_produto(self, nome, quantidade, preco):
        self.ID += 1
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

        novo_produto = {
            'ID': self.ID,
            'nome': self.nome,
            'quantidade': self.quantidade,
            'preco': self.preco
        }

        pilhaproduto.push(novo_produto)
        print(novo_produto)

    def mostrar_produto(self):
        itens = pilhaproduto._items

        for item in itens:
            print(f"ID: {item["ID"]} | Nome: {item["nome"]} | Quantidade: {item["quantidade"]} | Preço: {item["preco"]}")