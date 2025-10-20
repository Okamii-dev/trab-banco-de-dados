MENU_PRINCIPAL = """ 
========== MENU PRINCIPAL ==========
1 - INSERIR REGISTROS
2 - EDITAR REGISTROS
3 - EXCLUIR REGISTROS
4 - RELATÓRIOS
0 - SAIR
====================================
"""

MENU_INSERIR = """
========== MENU DE REGISTROS ==========
1. REGISTRAR ALUNO
2. REGISTRAR LIVRO
3. REGISTRAR EMPRÉSTIMO
0. VOLTAR AO MENU PRINCIPAL
=======================================
"""

MENU_EDITAR = """
=========== MENU DE EDIÇÃO ===========
1. EDITAR ALUNO
2. EDITAR LIVRO
3. EDITAR EMPRÉSTIMO
0. VOLTAR AO MENU PRINCIPAL
=======================================
"""

MENU_EXCLUIR = """
=========== MENU DE EXCLUSÃO ==========
1. EXCLUIR ALUNO
2. EXCLUIR LIVRO
0. VOLTAR AO MENU PRINCIPAL
=======================================
"""

MENU_RELATORIOS = """
=========== MENU DE RELATÓRIOS ===========
1. LISTAR TODOS OS ALUNOS
2. LISTAR TODOS OS LIVROS
3. LISTAR EMPRÉSTIMOS ATIVOS
0. VOLTAR AO MENU PRINCIPAL
=========================================
"""

def limpar_tela():
    from splash_screen import splash_screen
    from time import sleep
    import os

    sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')