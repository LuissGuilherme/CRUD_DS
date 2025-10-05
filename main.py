import sys
import banco as inventario
import sqlite3 


def mostrar_menu():
    print("---Estoque---")
    print("1 - Inserir Produtos")
    print("2 - Listar Produto")
    print("3 - Atualizar Produto")
    print("4 - Excluir Produto")
    print("0 - Sair")

def inserir():
    nome = input("Digite o nome do produto: ").strip()
     
    while True:
        try:
            quantidade = int(input("Digite a quantidade do produto: ").strip())
            break
        except ValueError:
            print("Quantidade inválida. Por favor, digite um número inteiro.")

    while True:
        try:
            preco = float(input("Digite o preço do produto (use '.' para centavos. Ex: 12.50): ").strip())
            break
        except ValueError:
            print("Preço inválido. Por favor, use um número (use '.' para centavos. Ex: 12.50).")
 
    inventario.inserir_produto(nome, quantidade, preco)
    input("\nPressione Enter para voltar ao menu...")

def listar():
   if inventario.verificacao_banco(): # Retorna True se estiver vazio
        print("\nO estoque está vazio.")
   else:
        inventario.listar_produtos()
        input("Pressione Enter para voltar ao menu...")
    
def atualizar():
    if inventario.verificacao_banco(): 
        print("\nO estoque está vazio, não há produtos para atualizar.")
        input("Pressione Enter para voltar ao menu...")
        return
    
    
    inventario.listar_produtos()
    while True: 
        try:
            id_produto = int(input("Digite o ID do produto que deseja atualizar: ").strip())
            if inventario.id_existe(id_produto):
                break 
            else:
                print(f"Erro: O ID '{id_produto}' não foi encontrado. Tente novamente.")

        except ValueError:
            print("ID inválido. Por favor, digite um número inteiro.")
    
    
    while True:
        try:
            id_produto = int(input("Digite o ID do produto que deseja atualizar: ").strip())
            break
        except ValueError:
            print("ID inválido. Por favor, digite um número.")
            
    # Pede as novas informações
    print(f"\n--- Editando Produto ID: {id_produto} ---")
    novo_nome = input("Digite o novo nome do produto: ").strip()

    while True:
        try:
            nova_quantidade = int(input("Digite a nova quantidade: ").strip())
            break
        except ValueError:
            print("Quantidade inválida. Por favor, digite um número inteiro.")
            
    while True:
        try:
            novo_preco = float(input("Digite o novo preço (ex: 12.50): ").strip())
            break
        except ValueError:
            print("Preço inválido. Por favor, use um número (use '.' para centavos).")
    
    # Chama a função do banco para atualizar
    inventario.atualizar_produtos(id_produto, novo_nome, nova_quantidade, novo_preco)
    input("\nPressione Enter para voltar ao menu...")
def excluir():

    if inventario.verificacao_banco(): 
        print("\nO estoque está vazio, não há produtos para excluir.")
        input("Pressione Enter para voltar ao menu...")
        return
        
    
    inventario.listar_produtos()
    
    
    while True:
        try:
            id_exclusao = int(input("Digite o ID do produto que deseja excluir: ").strip())
            break
        except ValueError:
            print("ID inválido. Por favor, digite um número inteiro.")
            
    
    inventario.excluir_produto(id_exclusao)
    input("\nPressione Enter para voltar ao menu...")

def main():
    inventario.iniciar_banco()
    while(True):
        mostrar_menu()
        opcao = input("Digite a opção:")
        match opcao:
            case "1":
                print("Inserir Produtos ")
                inserir()
            case "2":
                print("Listar Produtos ")  
                listar()
            case "3":
                print("Atualizar Produtos")
                atualizar()
            case "4":
                print("Excluir Produtos") 
                excluir() 
            case "0":
               sys.exit(0) 

main()