from produto import Produto
from cliente import Cliente
from resources import limpar_tela, continuar

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
    limpar_tela()

    match opcao:
   
        # CADASTRAR CLIENTE
        case '1':

            while True:

                nome_cliente = input("Digite seu nome: ").strip()
                
                if nome_cliente != '':
                    limpar_tela()
                    cliente.cadastrar_cliente(nome_cliente)
                    break
                else:
                    limpar_tela()
                    print("Erro! Digite um nome válido.")
                    continue


        # LISTAR CLIENTES    
        case '2': 
            cliente.listar_clientes()

        # CADASTRAR PRODUTOS
        case '3': 
            while True:    
                produto_cadastrar = input("Digite o nome do produto que deseja cadastrar: ")
                
                produto_quantidade = int(input("Digite a quantidade do produto: "))
                produto_preco = float(input("Digite o preço do produto: "))

                limpar_tela()

                produto.cadastrar_produto(produto_cadastrar, produto_quantidade, produto_preco)
                print("Produto Cadastrado com sucesso!")


        #LISTAR PRODUTOS
        case '4':
            produto.mostrar_produto()
            print()
            continuar()
            limpar_tela()


        #REALIZAR VENDAS
        case '5':
            cliente_venda = input('Digite o nome do cliente que está realizando a compra: ')


        #VER FILA DE VENDAS
        case '6':
            pass


        #DESFAZER ULTIMA OPERACAO
        case '7':
            pass


        #EXIBIR TOTAL DO ESTOQUE
        case '8':
            produto.valor_total_estoque()
            print()
            continuar()
            limpar_tela()


        case '9':
            pass

        #EXIBIR CLIENTES E VALORES TOTAIS GASTOS
        case '10':
            pass

        case '11':
            limpar_tela()
            print('Obrigado por usar nosso sistema! Volte sempre!')
            break

        #SE NENHUMA OPCAO
        case _:
            limpar_tela()
            print('Digite um digito válido!')
            continuar()
            limpar_tela()
            continue