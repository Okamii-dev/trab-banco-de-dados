from model.emprestimo import Emprestimo
from conexion.mysql_queries import MySQLQueries

class ControllerEmprestimo:
    def __init__(self):
        pass

    def registrar_emprestimo(self) -> Emprestimo:
        mysql = MySQLQueries(can_write=True)
        mysql.connect()

        try:
            id_leitor = input("Digite o ID do leitor: ")
            id_livro = input("Digite o ID do livro: ")
            data_emprestimo = input("Data do empréstimo (YYYY-MM-DD): ")
            data_devolucao = input("Data prevista de devolução (YYYY-MM-DD): ")

            query = f"""
                INSERT INTO emprestimo (id_leitor, id_livro, data_emprestimo, data_devolucao)
                VALUES ({id_leitor}, {id_livro}, '{data_emprestimo}', '{data_devolucao}');
            """
            mysql.execute_dml(query)
            print("✅ Empréstimo registrado com sucesso.")
            return Emprestimo(None, id_leitor, id_livro, data_emprestimo, data_devolucao)
        finally:
            mysql.close()

    def devolver_livro(self):
        mysql = MySQLQueries(can_write=True)
        mysql.connect()

        try:
            id_emprestimo = input("Digite o ID do empréstimo: ")
            data_real = input("Data real de devolução (YYYY-MM-DD): ")

            query = f"""
                UPDATE emprestimo
                SET data_dev_realizad = '{data_real}'
                WHERE id_emprestimo = {id_emprestimo};
            """
            mysql.execute_dml(query)
            print("✅ Devolução registrada.")
        finally:
            mysql.close()

    def excluir_emprestimo(self):
        mysql = MySQLQueries(can_write=True)
        mysql.connect()

        try:
            id_emprestimo = input("Digite o ID do empréstimo: ")
            query = f"DELETE FROM emprestimo WHERE id_emprestimo = {id_emprestimo};"
            mysql.execute_dml(query)
            print("✅ Empréstimo excluído.")
        finally:
            mysql.close()
