from datetime import date
from model.leitor import Leitor
from model.livro import Livro

class Emprestimo:
    def __init__(self, 
                 id: int = None, 
                 leitor: Leitor = None, 
                 livro: Livro = None, 
                 data_emprestimo: date = None, 
                 data_devolucao: date = None):
        self.set_id(id)
        self.set_leitor(leitor)
        self.set_livro(livro)
        self.set_data_emprestimo(data_emprestimo)
        self.set_data_devolucao(data_devolucao)

    def set_id(self, id: int):
        self.id = id
    def get_id(self) -> int:
        return self.id
    def set_leitor(self, leitor: Leitor):
        self.leitor = leitor
    def get_leitor(self) -> Leitor:
        return self.leitor
    def set_livro(self, livro: Livro):
        self.livro = livro
    def get_livro(self) -> Livro:
        return self.livro
    def set_data_emprestimo(self, data_emprestimo: date):
        self.data_emprestimo = data_emprestimo
    def get_data_emprestimo(self) -> date:
        return self.data_emprestimo
    def set_data_devolucao(self, data_devolucao: date):
        self.data_devolucao = data_devolucao
    def get_data_devolucao(self) -> date:
        return self.data_devolucao

    def to_string(self) -> str:
        return f'ID Empréstimo: {self.get_id()}, Leitor: ({self.get_leitor().to_string()}), Livro: ({self.get_livro()}), Data Empréstimo: {self.get_data_emprestimo()}, Data Devolução: {self.get_data_devolucao()}'