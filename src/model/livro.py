class Livro:
    def __init__(self, 
                 id: int = None, 
                 titulo: str = None, 
                 autor: str = None, 
                 editora: str = None,):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.editora = editora

        def set_id(self, id: int):
            self.id = id
        def get_id(self) -> int:
            return self.id
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

    def __repr__(self):
        return f"Livro(id={self.id}, titulo='{self.titulo}', autor='{self.autor}', editora='{self.editora}')"