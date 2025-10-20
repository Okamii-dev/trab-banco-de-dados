class Leitor:
    def __init__(self, 
                 id_leitor: int = None,
                 nome: str = None,
                 cpf: str = None,
                 telefone: str = None,
                 email: str = None):
        self.set_id_leitor(id_leitor)
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_telefone(telefone)
        self.set_email(email)

    # GETTERS E SETTERS
    def set_id_leitor(self, id_leitor: int):
        self.id_leitor = id_leitor
    def get_id_leitor(self) -> int:
        return self.id_leitor
    
    def set_nome(self, nome: str):
        self.nome = nome
    def get_nome(self) -> str:
        return self.nome
    
    def set_cpf(self, cpf: str):
        self.cpf = cpf
    def get_cpf(self) -> str:
        return self.cpf
    
    def set_telefone(self, telefone: str):
        self.telefone = telefone
    def get_telefone(self) -> str:
        return self.telefone
    
    def set_email(self, email: str):
        self.email = email
    def get_email(self) -> str:
        return self.email
    
    # REPRESENTAÇÃO EM STRING
    def to_string(self) -> str:
        return (
            f"ID Leitor: {self.get_id_leitor()} | "
            f"Nome: {self.get_nome()} | "
            f"CPF: {self.get_cpf()} | "
            f"Telefone: {self.get_telefone()} | "
            f"Email: {self.get_email()}"
        )
