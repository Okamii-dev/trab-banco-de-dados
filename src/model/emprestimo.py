from datetime import date
from model.leitor import Leitor
from model.livro import Livro

class Emprestimo:
    def __init__(self, 
                 id_emprestimo: int = None, 
                 leitor: Leitor = None, 
                 livro: Livro = None, 
                 data_emprestimo: date = None, 
                 data_devolucao_prevista: date = None,
                 data_devolucao_realizada: date = None):
        self.set_id_emprestimo(id_emprestimo)
        self.set_leitor(leitor)
        self.set_livro(livro)
        self.set_data_emprestimo(data_emprestimo)
        self.set_data_devolucao_prevista(data_devolucao_prevista)
        self.set_data_devolucao_realizada(data_devolucao_realizada)

    # GETTERS E SETTERS
    def set_id_emprestimo(self, id_emprestimo: int):
        self.id_emprestimo = id_emprestimo
    def get_id_emprestimo(self) -> int:
        return self.id_emprestimo
    
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
    
    def set_data_devolucao_prevista(self, data_devolucao_prevista: date):
        self.data_devolucao_prevista = data_devolucao_prevista
    def get_data_devolucao_prevista(self) -> date:
        return self.data_devolucao_prevista
    
    def set_data_devolucao_realizada(self, data_devolucao_realizada: date):
        self.data_devolucao_realizada = data_devolucao_realizada
    def get_data_devolucao_realizada(self) -> date:
        return self.data_devolucao_realizada

    # REPRESENTAÇÃO EM STRING
    def to_string(self) -> str:
        return (
            f"ID Empréstimo: {self.get_id_emprestimo()} | "
            f"Leitor: {self.leitor.get_nome() if self.leitor else 'N/A'} | "
            f"Livro: {self.livro.get_titulo() if self.livro else 'N/A'} | "
            f"Data Empréstimo: {self.get_data_emprestimo()} | "
            f"Devolução Prevista: {self.get_data_devolucao_prevista()} | "
            f"Devolução Realizada: {self.get_data_devolucao_realizada()}"
        )
