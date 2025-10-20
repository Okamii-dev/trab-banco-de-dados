select em.id_emprestimo,
        em.data_emprestimo,
        em.data_devolucao,
        le.nome as nome_leitor,
        li.titulo as titulo_livro
    from emprestimo em
    join leitor le on em.id_leitor = le.id_leitor
    join livro li on em.id_livro = li.id_livro
    ORDER BY em.data_emprestimo