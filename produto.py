from cliente import Cliente
from pilha import Pilha
from fila import Fila

fila_venda = Fila()
pilhaproduto = Pilha()
cliente = Cliente()

class Produto:
    def __init__(self):
        self.ID = 0
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
    
    def verificar_produto(self,ID=None):
        items = pilhaproduto._items
        for item in items:
            if ID == item["ID"]:
                return True
        return False
    
    def venda(self):
        
        cliente_venda = int(input('Digite o ID do cliente que está realizando a compra: '))
        if not cliente.verificar_cliente(cliente_venda):
            print("Cliente não encontrado!")
            return
        
        id_venda = int(input('Digite o ID do produto: '))
        quantidade_venda = int(input('Digite a quantidade: '))
        valor_gasto = 0
        items = pilhaproduto._items

        for i,item in enumerate(items):
            if id_venda == item["ID"]:
                print(item)
                if item["quantidade"] < quantidade_venda:
                    print("Quantidade de produtos insuficientes")
                    break
                item["quantidade"] -= quantidade_venda

                if item["quantidade"] == 0:

                    items.pop(i)

                valor_gasto = quantidade_venda*(item['preco'])

                nova_venda = {
                    'nome': item["nome"],
                    'quantidade': quantidade_venda,
                    'preco': valor_gasto     
                }
                cliente.venda(cliente_venda,valor_gasto)
                fila_venda.enqueue(nova_venda)
                print("Venda Realizada com sucesso!")
                print(f'Valor total: R$ {valor_gasto:.2f}')
                return

            return
        
        print("Produto não encontrado")

    def desfazer_venda(self):
        produto=fila_venda.front()
        fila_venda.dequeue()
        valor=produto['preco']
        cliente.desfazer_venda(valor)
        print("Venda desfeita")


    def todos_itens_vendidos(self):
         
        items = fila_venda._items

        for item in items:
            print(f"Nome: {item["nome"]} | Quantidade: {item["quantidade"]} | Valor Total: {item["preco"]}")

    def total_valor_gasto(self):
        items = fila_venda._items
        total=0
        for item in items:
            total+=item["preco"]
        print(f"Total de vendas: {total:.2f}")


    def pesquisar_produto(self):
        pesquisaID = int(input("Digite ID para fazer a pesquisa do produto: "))
        pesquisaProdutoID = pilhaproduto._items

        for i in pesquisaProdutoID:
            if pesquisaID == i["ID"]:
                print(i)
            else:
                print("errou")

   




# Escolha: 3
# Digite o ID do produto: 101
# Digite a quantidade: 2
# Venda realizada com sucesso!
# (Valor total: R$7000.00) 