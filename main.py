from produto import Produto
from cliente import Cliente
import os
import time
produto = Produto()
cliente = Cliente()

# 1. Cadastrar cliente 
# 2. Listar clientes 
# 3. Cadastrar produto 
# 4. Listar produtos do estoque 
# 5. Realizar venda 
# 6. Visualizar fila de vendas 
# 7. Desfazer última operação (pilha) 
# 8. Exibir valor total do estoque 
# 9. Exibir valor total de vendas realizadas 
# 10. Exibir clientes e valores totais gastos 
# 11. Sair

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
        case '1':
            nome_cliente = input("Digite seu nome: ").strip()
            if nome_cliente.replace("","").isalpha() == True:
                print("Nome cadastrado com sucesso!")
            
            else:
                print("Erro! Digite um nome válido")
            cliente.cadastrar_cliente(nome_cliente)
     
        case '2':
            produtoCadastrar = input("Digite o nome do produto: ")
            produtoQuantidade = int(input("Digite a quantidade do produto: "))
            produtoPreco = float(input("Digite o preço do produto: "))
            produto.cadastrarproduto(produtoCadastrar, produtoQuantidade, produtoPreco)
           # ID = int(input("Digite ID do produto: "))
            print("Produto Cadastrado com sucesso!")
        
        case '4':
            print("--- ESTOQUE ATUAL --- ")
            produto.mostrarproduto()

        case '5':
            cliente.listar_clientes()
        case _:
            os.system('cls')
            input('Digite apenas um digito válido! Pressione ENTER para continuar')
            os.system('cls')
            continue
