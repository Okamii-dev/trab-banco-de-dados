
#Classe MySQLQueries — adaptada do modelo OracleQueries (Prof. Howard Roatti)

import mysql.connector

class MySQLQueries:
    def __init__(self, can_write: bool = False):
        """
        Inicializa a classe e define os parâmetros básicos da conexão.
        :param can_write: define se a conexão pode executar comandos de escrita.
        """
        self.can_write = can_write
        self.host = "localhost"
        self.database = "sistema_biblioteca"

        # Lê o arquivo de autenticação contendo user e password.
        # O arquivo deve estar em: src/conexion/passphrase/authentication.mysql
        # Formato esperado: user,senha  (sem espaços)
        with open("src/conexion/passphrase/authentication.mysql", "r") as f:
            self.user, self.password = f.read().strip().split(",")

        self.conn = None
        self.cursor = None

    # ---------------------------------------------------------------------
    def connect(self):
        """
        Estabelece a conexão com o banco de dados MySQL e cria o cursor.
        Retorna o cursor para execução de comandos SQL.
        """
        self.conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.conn.cursor()
        return self.cursor

    # ---------------------------------------------------------------------
    def execute_ddl(self, query: str):
        """
        Executa comandos DDL (Data Definition Language), como:
        CREATE, ALTER, DROP.
        Esses comandos alteram a estrutura do banco de dados.
        """
        self.cursor.execute(query)

    # ---------------------------------------------------------------------
    def execute_dml(self, query: str):
        """
        Executa comandos DML (Data Manipulation Language), como:
        INSERT, UPDATE, DELETE.
        Esses comandos manipulam dados dentro das tabelas.
        O commit confirma a transação no banco.
        """
        if not self.can_write:
            raise Exception("Esta conexão não tem permissão de escrita.")
        self.cursor.execute(query)
        self.conn.commit()

    # ---------------------------------------------------------------------
    def fetch(self, query: str):
        """
        Executa comandos SELECT (Data Query Language).
        Retorna uma lista de tuplas contendo os registros recuperados.
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    # ---------------------------------------------------------------------
    def close(self):
        """
        Fecha o cursor e a conexão com o banco de dados MySQL.
        Deve ser chamado após concluir as operações no banco.
        """
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
