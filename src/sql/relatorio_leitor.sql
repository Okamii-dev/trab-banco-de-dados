select le.id_leitor,
        le.CPF,
        le.nome,
        le.email,
        le.telefone
    from leitor le
    ORDER BY le.nome