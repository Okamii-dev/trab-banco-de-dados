from model.livro import Livro
from conexion.mysql_queries import MySQLQueries

class ControllerLivro:
    def __init__(self):
        pass

    def cadastrar_livro(self) -> Livro:
        mysql = MySQLQueries(can_write=True)
        mysql.connect()

        try:
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            editora = input("Digite a editora: ")
            categoria = input("Digite a categoria: ")
            quantidade = input("Digite a quantidade: ")

            query = f"""
                INSERT INTO livro (titulo, autor, editora, categoria, quantidade)
                VALUES ('{titulo}', '{autor}', '{editora}', '{categoria}', {quantidade});
            """
            mysql.execute_dml(query)
            print("✅ Livro cadastrado com sucesso.")
            return Livro(None, titulo, autor, editora, categoria, quantidade)
        finally:
            mysql.close()

    def atualizar_livro(self) -> Livro:
        mysql = MySQLQueries(can_write=True)
        mysql.connect()

        try:
            id_livro = input("Digite o ID do livro a ser atualizado: ")
            titulo = input("Novo título: ")
            autor = input("Novo autor: ")
            editora = input("Nova editora: ")
            categoria = input("Nova categoria: ")
            quantidade = input("Nova quantidade: ")

            query = f"""
                UPDATE livro
                SET titulo='{titulo}', autor='{autor}', editora='{editora}',
                    categoria='{categoria}', quantidade={quantidade}
                WHERE id_livro = {id_livro};
            """
            mysql.execute_dml(query)
            print("✅ Livro atualizado com sucesso.")
            return Livro(id_livro, titulo, autor, editora, categoria, quantidade)
        finally:
            mysql.close()

    def excluir_livro(self):
        mysql = MySQLQueries(can_write=True)
        mysql.connect()

        try:
            id_livro = input("Digite o ID do livro a ser excluído: ")
            query = f"DELETE FROM livro WHERE id_livro = {id_livro};"
            mysql.execute_dml(query)
            print("✅ Livro excluído com sucesso.")
        finally:
            mysql.close()
