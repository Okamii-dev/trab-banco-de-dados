class Leitor:
    def __init__(self, 
                 id: int = None,
                 nome: str = None, ):
        self.set_id(id)
        self.set_nome(nome)

    def set_id(self, id: int):
        self.id = id
    def get_id(self) -> int:
        return self.id 
    def set_nome(self, nome: str):
        self.__nome = nome
    def get_nome(self) -> str:
        return self.__nome
    
    def to_string(self) -> str:
        return f'Matrícula: {self.get_id()}, Nome: {self.get_nome()}'