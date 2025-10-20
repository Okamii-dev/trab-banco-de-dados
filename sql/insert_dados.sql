-- Inserir leitores
INSERT INTO leitor (nome, cpf, telefone, email)
VALUES
("Marcelo Mindas", "180.081.097-00", "27 99659-2133", "mindasmarcelo@gmail.com"),
("Ester Bertolani",'563.57.963-04', "27 99456-3694", "bertolaniester@hotmail.com"),
("Vanderson Almeia", '122.353.654-78', '27 99886-0906' , 'almeidavanderson@gmail.com'), 
("Alexsander Amorim", '454.231.567-66', '27 99688-5261', 'amorimalexsander@gmail.com');

-- Inserir livros
INSERT INTO Livro (titulo, autor, editora, categoria, quantidade)
VALUES
('Dom Casmurro', 'Machado de Assis', 'Record', 'Romance', 1),
('O Cortiço', 'Aluísio Azevedo', 'Saraiva', 'Realismo', 2),
('Capitães da Areia', 'Jorge Amado', 'Companhia das Letras', 'Romance', 2);

-- Inserir empréstimos
INSERT INTO emprestimo (id_leitor, id_livro, data_emprestimo, data_devolucao_prevista, data_devolucao_realizada)
VALUES
(1, 1, '2025-10-15', '2025-10-25', '2025-10-25'),
(2, 3, '2025-10-15', '2025-10-25', '2025-10-25'),
(3, 2, '2025-10-15', '2025-10-25', '2025-10-25');

SELECT * FROM emprestimo;







