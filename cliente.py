from pilha import Pilha

pilha_clientes=Pilha()
class Cliente:
    def __init__(self):
        self.id=0
        self.nome=None
        self.clientes={}

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
            print(pilha_clientes)