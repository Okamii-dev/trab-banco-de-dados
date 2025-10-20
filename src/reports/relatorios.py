from conexion.mysql_queries import MySQLQueries

class Relatorios:

    def __init__(self):

        #ABRE O ARQUIVO COM A CONSULTA E ASSOCIA A UM ATRIBUTO
        with open("sql/relatorios_livro.sql") as f:
            self.relatorio_livro_query = f.read()
        with open("sql/relatorios_leitor.sql") as f:
            self.relatorio_leitor_query = f.read()
        with open("sql/relatorios_emprestimo.sql") as f:
            self.relatorio_emprestimo_query = f.read()

    def get_relatorio_livro(self):
        mysql = MySQLQueries()
        mysql.connect()
        print(mysql.fetch(self.relatorio_livro_query))
        input("Pressione Enter para continuar...")
        #DPS DESSE PRINT, PRECISA APERTAR ENTER PRA VOLTAR PRO MENU
        #POR CAUDA DO CLEAR SCREEN
    
    def get_relatorio_leitor(self):
        mysql = MySQLQueries()
        mysql.connect()
        print(mysql.fetch(self.relatorio_leitor_query))
        input("Pressione Enter para continuar...")
        #DPS DESSE PRINT, PRECISA APERTAR ENTER PRA VOLTAR PRO MENU
        #POR CAUDA DO CLEAR SCREEN

    def get_relatorio_emprestimo(self):
        mysql = MySQLQueries()
        mysql.connect()
        print(mysql.fetch(self.relatorio_emprestimo_query))
        input("Pressione Enter para continuar...")
        #DPS DESSE PRINT, PRECISA APERTAR ENTER PRA VOLTAR PRO MENU
        #POR CAUDA DO CLEAR SCREEN