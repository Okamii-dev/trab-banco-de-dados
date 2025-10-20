select li.id_livro,
        li.titulo,
        li.autor,
        li.ano_publicacao,
        li.editora
    from livro li
    ORDER BY li.titulo