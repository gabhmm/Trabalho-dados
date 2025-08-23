from produto import Produto
from cliente import Cliente
import os

produto = Produto()
cliente = Cliente()

while True:
    print("1 - Cadastrar Cliente: ")
    print("2 - Listar Clientes: ")
    print("3 - Cadastrar Produto: ")
    print("4 - Listar produtos ")
    print("5 - Realizar venda ")
    print("6 - Ver fila de vendas : ")
    print("7 - Desfazer última operação: ")
    print("8 - Exibir valor total do estoque : ")
    print("9 - Exibir valor total de vendas realizadas")
    print("10 - Exibir clientes e valores totais gastos")
    print("11 - Sair")

    opcao = input("Escolha a opção desejada: ")



    match opcao:
   
        # CADASTRAR CLIENTE
        case '1': 
            nome_cliente = input("Digite seu nome: ").strip()
            if nome_cliente.replace("","").isalpha() == True:
                print("Nome cadastrado com sucesso!")
                cliente.cadastrar_cliente(nome_cliente)            
            else:
                print("Erro! Digite um nome válido")



        # LISTAR CLIENTES    
        case '2': 
            cliente.listar_clientes()


        # CADASTRAR PRODUTOS
        case '3': 
            produtoCadastrar = input("Digite o nome do produto: ")
            produtoQuantidade = int(input("Digite a quantidade do produto: "))
            produtoPreco = float(input("Digite o preço do produto: "))
            produto.cadastrarproduto(produtoCadastrar, produtoQuantidade, produtoPreco)
           # ID = int(input("Digite ID do produto: "))
            print("Produto Cadastrado com sucesso!")

        #LISTAR PRODUTOS
        case '4':
            print("--- ESTOQUE ATUAL --- ")
            produto.mostrarproduto()


        #REALIZAR VENDAS
        case '5':
            pass


        #VER FILA DE VENDAS
        case '6':
            pass


        #DESFAZER ULTIMA OPERACAO
        case '7':
            pass


        #EXIBIR TOTAL DO ESTOQUE
        case '8':
            pass


        case '9':
            pass

        #EXIBIR CLIENTES E VALORES TOTAIS GASTOS
        case '10':
            pass


        #SE NENHUMA OPCAO
        case _:
            os.system('cls')
            input('Digite um digito válido! Pressione ENTER para continuar. ')
            os.system('cls')
            continue