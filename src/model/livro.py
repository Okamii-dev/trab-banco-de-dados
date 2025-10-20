class Livro:
    def __init__(self, 
                 id_livro: int = None, 
                 titulo: str = None, 
                 autor: str = None, 
                 editora: str = None,
                 categoria: str = None,
                 quantidade: int = 1):
        self.set_id_livro(id_livro)
        self.set_titulo(titulo)
        self.set_autor(autor)
        self.set_editora(editora)
        self.set_categoria(categoria)
        self.set_quantidade(quantidade)

    # GETTERS E SETTERS
    def set_id_livro(self, id_livro: int):
        self.id_livro = id_livro
    def get_id_livro(self) -> int:
        return self.id_livro
    
    def set_titulo(self, titulo: str):
        self.titulo = titulo
    def get_titulo(self) -> str:
        return self.titulo
    
    def set_autor(self, autor: str):
        self.autor = autor
    def get_autor(self) -> str:
        return self.autor
    
    def set_editora(self, editora: str):
        self.editora = editora
    def get_editora(self) -> str:
        return self.editora
    
    def set_categoria(self, categoria: str):    
        self.categoria = categoria
    def get_categoria(self) -> str:
        return self.categoria
    
    def set_quantidade(self, quantidade: int):
        self.quantidade = quantidade
    def get_quantidade(self) -> int:
        return self.quantidade
    
    # REPRESENTAÇÃO EM STRING
    def to_string(self) -> str:
        return (
            f"ID Livro: {self.get_id_livro()} | "
            f"Título: {self.get_titulo()} | "
            f"Autor: {self.get_autor()} | "
            f"Editora: {self.get_editora()} | "
            f"Categoria: {self.get_categoria()} | "
            f"Quantidade: {self.get_quantidade()}"
        )
