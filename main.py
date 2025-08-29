from produto import Produto
from cliente import Cliente
from pilha import Pilha
from resources import limpar_tela, continuar

produto = Produto()
cliente = Cliente()
pilha_acoes = Pilha()

while True:
    print("1 - Cadastrar Cliente ")
    print("2 - Listar Clientes ")
    print("3 - Cadastrar Produto ")
    print("4 - Listar produtos ")
    print("5 - Realizar venda ")
    print("6 - Ver fila de vendas ")
    print("7 - Desfazer última operação ")
    print("8 - Exibir valor total do estoque ")
    print("9 - Exibir valor total de vendas realizadas")
    print("10 - Exibir clientes e valores totais gastos")
    print("11 - Pesquisar Produto")
    print("12 - Sair")

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
                    pilha_acoes.push("cadastrar_cliente")
                    break
                else:
                    limpar_tela()
                    print("Erro! Digite um nome válido.")
                    continue


        # LISTAR CLIENTES    
        case '2':
            limpar_tela()
            print("LISTA DE CLIENTES:\n")
            cliente.listar_clientes()          
            continuar()
            limpar_tela()


        # CADASTRAR PRODUTOS
        case '3': 
            produto_cadastrar = input("Digite o nome do produto que deseja cadastrar: ")
            
            while True:
                try:
                    produto_quantidade = int(input("Digite a quantidade do produto: "))
                    if produto_quantidade > 0:
                        break
                    else:
                        print("A quantidade deve ser maior que zero.")
                except ValueError:
                    print("Por favor, digite apenas números inteiros para a quantidade.")
            
            while True:
                try:
                    produto_preco = float(input("Digite o valor do produto: ").replace(",", "."))
                    if produto_preco > 0:
                        break
                    else:
                        print("O valor deve ser maior que zero.")
                except ValueError:
                    print("Por favor, digite apenas números para o valor do produto.")        

            limpar_tela()

            produto.cadastrar_produto(produto_cadastrar, produto_quantidade, produto_preco)
            pilha_acoes.push("cadastrar_produto")


        #LISTAR PRODUTOS
        case '4':
            produto.mostrar_produto()
            print()
            continuar()
            limpar_tela()


        #REALIZAR VENDAS
        case '5':
            produto.venda()
            pilha_acoes.push("venda")
            continuar()
            limpar_tela()

        #VER FILA DE VENDAS
        case '6':
            limpar_tela()
            print("--- VENDAS REALIZADAS --- \n")
            produto.todos_itens_vendidos()
            continuar()
            limpar_tela()
            
        #DESFAZER ULTIMA OPERACAO
        case '7':
            if pilha_acoes.is_empty():
                print("Não existe alteração feita")
                continuar()
                limpar_tela()
                continue
            else:
                ultima_acao=pilha_acoes.peek()
                if ultima_acao=="cadastrar_cliente":
                    cliente.excluir_conta()
                    pilha_acoes.pop()
                    print(f"Cliente excluido!")
                if ultima_acao=="cadastrar_produto":
                    produto.excluir_produto()
                    pilha_acoes.pop()
                    print(f"Produto Excluido")
                if ultima_acao=="venda":
                    produto.desfazer_venda()
                    pilha_acoes.pop()


        #EXIBIR TOTAL DO ESTOQUE
        case '8':
            produto.valor_total_estoque()
            print()
            continuar()
            limpar_tela()


        case '9':
            limpar_tela()
            print("Total de vendas realizadas:")
            produto.total_valor_gasto()
            continuar()
            limpar_tela()



        #EXIBIR CLIENTES E VALORES TOTAIS GASTOS
        case '10':
            limpar_tela()
            print("--- CLIENTES E VALORES GASTOS--- \n")            
            cliente.gastos()
            continuar()
            limpar_tela()

        case '11':
            produto.pesquisar_produto()

            #pass
        case '12':
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