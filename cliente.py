from pilha import Pilha

class Cliente:
    def __init__(self):
        self.id=0
        self.nome=None
        self.clientes={}
        self.gasto = 0

    def cadastrar_cliente(self,nome):
        self.id+=1
        self.nome=nome

        novo_cliente = {
            'ID': self.id,
            'nome': self.nome,
        }

        pilha_clientes.push(novo_cliente)
        print(f"Cliente {nome} cadastrado!")
        print(f"Seu id é {self.id}.")
        return

    def listar_clientes(self):
        items = pilha_clientes._items

        for item in items:
            print(f"ID: {item["ID"]} | Nome: {item["nome"]}")

    def ultimo_cliente(self):
        ultimo_cliente = pilha_clientes.peek()
        return ultimo_cliente

    def excluir_conta(self):
        pilha_clientes.pop()
        return 
    
    def venda(self,valor):
        self.gasto += valor
        
        return self.gasto

pilha_clientes = Pilha()