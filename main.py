from produto import Produto
from cliente import Cliente

produto = Produto()
cliente = Cliente()

while True:
    print("0 - Cadastrar Cliente: ")
    print("1 - Cadastrar Produto: ")
    print("2 - Listar produtos ")
    print("3 - Realizar venda ")
    print("4 - Ver fila de vendas : ")
    print("5 - Desfazer última operação: ")
    print("6 - Exibir valor total do estoque : ")
    print("7 - Exibir valor total de vendas realizadas")
    print("8 - Sair ")
    opcao = int(input("Escolha a opção desejada: "))

    match opcao:
        case 0 :
            nome_cliente = input("Digite seu nome: ").strip()
            if nome_cliente.replace("","").isalpha() == True:
                print("Nome cadastrado com sucesso!")
            
            else:
                print("Erro! Digite um nome válido")
            cliente.cadastrar_cliente(nome_cliente)
     
        case 1:
            produtoCadastrar = input("Digite o nome do produto: ")
            produtoQuantidade = int(input("Digite a quantidade do produto: "))
            produtoPreco = float(input("Digite o preço do produto: "))
            produto.cadastrarproduto(produtoCadastrar, produtoQuantidade, produtoPreco)
           # ID = int(input("Digite ID do produto: "))
            print("Produto Cadastrado com sucesso!")
        
        case 2:
            print("--- ESTOQUE ATUAL --- ")
            produto.mostrarproduto()

        case 4:
            cliente.listar_clientes()