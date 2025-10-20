from conexion.mysql_queries import MySQLQueries

db = MySQLQueries(can_write=True)
db.connect()

db.execute_dml("""
    INSERT INTO Leitor (nome, cpf, telefone, email) VALUES
    ('Mindas', '123.456.789-00', '279999999', 'mindas@email.com'),
    ('Maria', '321.654.987-00', '279988888', 'maria@email.com'),
    ('João', '111.222.333-44', '279977777', 'joao@email.com')
""")

dados = db.fetch("SELECT * FROM Leitor;")
for linha in dados:
    print(linha)
db.close()
