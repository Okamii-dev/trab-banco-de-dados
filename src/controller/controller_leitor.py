from model.leitor import Leitor
from conexion.mysql_queries import MySQLQueries

class ControllerLeitor:
    def __init__(self):
        pass

    def cadastrar_leitor(self) -> Leitor:
        mysql = MySQLQueries(can_write=True)
        mysql.connect()

        try:
            cpf = input("Digite o CPF do leitor: ")

            if not self.existe_leitor(mysql, cpf):
                nome = input("Digite o nome do leitor: ")
                email = input("Digite o email do leitor: ")
                telefone = input("Digite o telefone do leitor: ")

                mysql.execute_dml(
                    f"""
                    INSERT INTO leitor (nome, cpf, email, telefone)
                    VALUES ('{nome}', '{cpf}', '{email}', '{telefone}');
                    """
                )

                novo_leitor = Leitor(None, nome, cpf, email, telefone)
                print("✅ Leitor cadastrado com sucesso!")
                print(novo_leitor.to_string())
                return novo_leitor
            else:
                print("⚠️ Leitor já cadastrado.")
                return None
        except Exception as e:
            print(f"❌ Erro ao cadastrar leitor: {e}")
        finally:
            mysql.close()

    def atualizar_leitor(self) -> Leitor:
        mysql = MySQLQueries(can_write=True)
        mysql.connect()

        try:
            cpf = input("Digite o CPF do leitor a ser atualizado: ")

            if self.existe_leitor(mysql, cpf):
                nome = input("Novo nome: ")
                email = input("Novo email: ")
                telefone = input("Novo telefone: ")

                mysql.execute_dml(
                    f"""
                    UPDATE leitor 
                    SET nome = '{nome}', email = '{email}', telefone = '{telefone}'
                    WHERE cpf = '{cpf}';
                    """
                )

                leitor_atualizado = Leitor(None, nome, cpf, email, telefone)
                print("✅ Leitor atualizado com sucesso!")
                print(leitor_atualizado.to_string())
                return leitor_atualizado
            else:
                print("⚠️ Leitor não encontrado.")
        except Exception as e:
            print(f"❌ Erro ao atualizar leitor: {e}")
        finally:
            mysql.close()

    def excluir_leitor(self):
        mysql = MySQLQueries(can_write=True)
        mysql.connect()

        try:
            cpf = input("Digite o CPF do leitor a ser excluído: ")

            if self.existe_leitor(mysql, cpf):
                mysql.execute_dml(
                    f"DELETE FROM leitor WHERE cpf = '{cpf}';"
                )
                print("🗑️ Leitor excluído com sucesso.")
            else:
                print("⚠️ Leitor não encontrado.")
        except Exception as e:
            print(f"❌ Erro ao excluir leitor: {e}")
        finally:
            mysql.close()

    def existe_leitor(self, mysql: MySQLQueries, cpf: str) -> bool:
        query = f"SELECT 1 FROM leitor WHERE cpf = '{cpf}';"
        resultado = mysql.fetch(query)
        return len(resultado) > 0
