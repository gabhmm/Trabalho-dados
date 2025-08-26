from pilha import Pilha

pilha_clientes = Pilha()
pilha_id=Pilha()

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
            'gastos':self.gasto
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
        print("vai excluir")
        return 
    
    def verificar_cliente(self,id=None):
        items = pilha_clientes._items
        for item in items:
            if id == item["ID"]:
                return True
            return False
    def venda(self,id=None,valor=None):
        items = pilha_clientes._items
        for item in items:
            

            if id == item["ID"]:
                pilha_id.push(id)
                item["gastos"] += valor
                return(f"Nome: {item["nome"]} | Valor Gasto: R$ {item["gastos"]:.2f}")

            print("Cliente não encontrado!")

    def desfazer_venda(self,valor=None):
        id=pilha_id.peek()
        pilha_id.pop(id)

        items = pilha_clientes._items

        for item in items:
            
            if id == item["ID"]:
                item["gastos"] -= valor
