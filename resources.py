import os

def limpar_tela():
    return os.system('cls' if os.name == 'nt' else 'clear')

def continuar():
    input("Pressione ENTER para continuar. ")
