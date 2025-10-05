
import sqlite3

conexao = sqlite3.connect("Inventario.db")
cursor = conexao.cursor()


def iniciar_banco():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT UNIQUE NOT NULL,
        quantidade INTEGER NOT NULL,
        preco REAL NOT NULL
        )
    """)

# Verificação se há produtos no banco
def verificacao_banco():
    cursor.execute("SELECT COUNT(*) FROM produtos")
    count = cursor.fetchone()[0]
    return count == 0

# CREATE
def inserir_produto(nome,quantidade,preco):
    try:
        cursor.execute("INSERT INTO produtos (nome,quantidade,preco) VALUES(?,?,?)",
                       (nome,quantidade,preco))
        conexao.commit()
        print("Produto adicionado com sucesso")
    except sqlite3.IntegrityError:
        print("Erro: Produto já existente na tabela")

# READ
def listar_produtos():
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    print("\n--- LISTA DE PRODUTOS ---")
    print("ID | NOME | QUANTIDADE | PREÇO")
    for p in produtos:
        print(f"{p[0]} | {p[1]} | {p[2]} | R${p[3]:.2f}")
    print("-------------------------")


#UDPATE
def atualizar_produtos(id_produto,novo_nome,nova_quantidade, novo_preco):
    cursor.execute("UPDATE produtos SET nome =?, quantidade=?, preco=? WHERE id=?",
        (novo_nome,nova_quantidade, novo_preco, id_produto))

    if cursor.rowcount > 0:
        print("Produto atualizado com sucesso!")
        conexao.commit()
    else:
        print("Produto não encontrado na tabela!")

#DELETE
def excluir_produto(id_produto):
    cursor.execute("DELETE FROM produtos WHERE id = ?",(id_produto,))

    if cursor.rowcount > 0:
        print("Produto excluido com sucesso!")
        conexao.commit()
    else:
        print("Produto não encontrado na tabela!")

def fechar_banco():
    conexao.commit()
    conexao.close()