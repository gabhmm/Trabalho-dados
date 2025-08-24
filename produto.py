
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

    def valor_total_estoque(self):
        valor = 0

        items = pilhaproduto._items

        for item in items:
            valor += (item["preco"] * item["quantidade"])

        print(f'Valor total em estoque: R$ {valor:.2f} ')

    def mostrar_produto(self):
        print("--- ESTOQUE ATUAL --- \n")

        items = pilhaproduto._items

        for item in items:
            print(f"ID: {item["ID"]} | Nome: {item["nome"]} | Quantidade: {item["quantidade"]} | Preço: {item["preco"]}")

    def excluir_produto(self):
        pilhaproduto.pop()
        return
    
    def venda(self):

        id_venda = int(input('Digite o ID do produto: '))
        quantidade_venda = int(input('Digite a quantidade: '))


        items = pilhaproduto._items

        for i,item in enumerate(items):

            if id_venda == item["ID"]:

                item["quantidade"] -= quantidade_venda

                if item["quantidade"] == 0:

                    items.pop(i)

                print(f'Valor total: R$ {(quantidade_venda*(item['preco'])):.2f}')



# Escolha: 3
# Digite o ID do produto: 101
# Digite a quantidade: 2
# Venda realizada com sucesso!
# (Valor total: R$7000.00)
