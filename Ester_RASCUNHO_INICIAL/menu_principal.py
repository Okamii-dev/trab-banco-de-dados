# Rascunho de MENU

from splash_screen import splash_screen

# aqui tem que fazer alguma coisa pra aparecer só a tela inicial aí depois o menu aparece
# (tipo qnd o usuário dá enter ou sla)

opcao = None

while True:
    print(" ===== MENU PRINCIPAL =====\n"
          " 1. Relatórios\n"
          " 2. Inserir Registros\n"
          " 3. Alterar Registros\n"
          " 4. Remover Resgistros\n"
          " 5. SAIR\n")
    opcao = int(input(" | Opção: "))
    # limpar opcao dps

    match opcao:
        case 1:

            # submenu de relatórios

            print("lalala")

        case 2:

            # submenu de inserção:
            while True:
                print(" ===== Inserir Registros =====\n"
                      " 1. Cadastrar novo Aluno\n"
                      " 2. Cadastrar novo Livro\n"
                      " 3. Realizar novo Empréstimo\n"
                      " 4. (se tiver mais alguma coisa)\n"
                      " 5. VOLTAR\n")
                opcao = int(input(" | Opção: "))
            # outro match/case
                match opcao:
                    case 5:
                        break

        case 3:

            # submenu de alteração:
            while True:
                print(" ===== Alterar Registros =====\n"
                      " 1. Alterar dados de Aluno\n"
                      " 2. Alterar dados de Livro\n"
                      " 3. Alterar dados de Empréstimo\n"
                      " 4. (se tiver mais alguma coisa)\n"
                      " 5. VOLTAR\n")
                opcao = int(input(" | Opção: "))
            # outro match/case
                match opcao:
                    case 5:
                        break

        case 4:

            # submenu de remoção:
            while True:
                print(" ===== Excluir Registros =====\n"
                      " 1. Excluir Aluno\n"
                      " 2. Excluir Livro\n"
                      " 3. Excluir Empréstimo (pode?) \n"
                      " 4. (se tiver mais alguma coisa)\n"
                      " 5. VOLTAR\n")
                opcao = int(input(" | Opção: "))
                # outro match/case
                match opcao:
                    case 5:
                        break

        case 5:
            print("Tchauzinho :D")
            break

        case _:
            print("ERRADO!!!")
