# FILE/FOLDER DEDICADO A ORGANIZAÇÃO DE TAREFAS PARA MELHOR EXECUÇÃO DO PROJETO

## Objetivo

    Desenvolver um mini sistema de estoque e vendas utilizando Programação Orientada a Objetos(POO) e estruturas de dados clássicas: Lista, Pilha e Fila.
    O sistema deve ser executado no terminal e permitir interação do usuário.

## Descrição

    Você deverá implementar um sistema que gerencie um pequeno estoque de produtos. O usuário
    poderá cadastrar clientes, cadastrar produtos, listar estoque, realizar vendas e visualizar o
    histórico de operações.
    trabalho tem como propósito fixar os conceitos de listas, pilhas, filas e POO em um caso prático.

## Estruturas obrigatórias
    ● Classe Produto: id, nome, quantidade e preço.
    ● Classe Cliente: id, nome.
    ● Lista para armazenar os produtos do estoque.
    ● Fila: para registrar as vendas realizadas em ordem de chegada.
    ● Pilha: para permitir o desfazer da última operação (cadastro ou venda).
    ● Menu no terminal: interação do usuário com opções numéricas.

## Funcionalidades mínimas
    1. Cadastrar cliente
    2. Listar clientes
    3. Cadastrar produto
    4. Listar produtos do estoque
    5. Realizar venda
    6. Visualizar fila de vendas
    7. Desfazer última operação (pilha)
    8. Exibir valor total do estoque
    9. Exibir valor total de vendas realizadas
    10. Exibir clientes e valores totais gastos
    11. Sair

## Funcionalidades extras (vale 0,5 pontos a mais na média)
    1. Pesquisar produtos por nome ou id.
    2. Salvar e carregar os dados do estoque em arquivo .txt

## Exemplo de execução

    ===== MENU ESTOQUE =====
    1 - Cadastrar produto
    2 - Listar produtos
    3 - Realizar venda
    4 - Ver fila de vendas
    5 - Desfazer última operação
    6 - Exibir valor total do estoque
    7 - Exibir valor total de vendas realizadas
    8 - Sair
---
    Escolha: 1
    Digite o nome do produto: Notebook
    Digite a quantidade: 5
    Digite o preço: 3500
    Produto cadastrado com sucesso!
    (ID gerado: 101)
---

    Escolha: 2
    --- ESTOQUE ATUAL ---
    ID: 101 | Nome: Notebook | Quantidade: 5 | Preço: R$3500.00
---

    Escolha: 3
    Digite o ID do produto: 101
    Digite a quantidade: 2
    Venda realizada com sucesso!
    (Valor total: R$7000.00)
---

    Escolha: 4
    --- FILA DE VENDAS ---
    Produto: Notebook | Quantidade: 2 | Valor Total: R$7000.00
---

    Escolha: 5
    Última operação desfeita com sucesso!
    (Venda do produto "Notebook" cancelada)
---

    Escolha: 6
    Valor total do estoque: R$17500.00
---
Escolha: 7
    Valor total de vendas realizadas: R$0.00
--- 
    Escolha: 8
    Saindo do sistema... Até logo!
---

## Critérios de avaliação
1. Estruturas de dados implementadas corretamente (listas, fila e pilha).
2. Organização do código em POO (classes bem definidas).
3. Clareza na interação com o usuário (menus e mensagens).
4. Funcionalidades mínimas funcionando.
5. Funcionalidades extras valem pontos adicionais.
6. O programa deve tratar situações inesperadas sem quebrar a execução.
○ Se o usuário tentar vender mais do que o estoque disponível
○ Se o usuário informar um ID de produto inexistente
○ Se o usuário digitar uma opção inválida no menu