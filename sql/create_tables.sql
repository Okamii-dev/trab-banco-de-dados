
CREATE DATABASE sistema_biblioteca;
USE sistema_biblioteca;

CREATE TABLE Leitor (
    id_leitor INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    cpf VARCHAR(16) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL
);

CREATE TABLE Livro (
    id_livro INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(30) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    editora VARCHAR(30) NOT NULL,
    categoria VARCHAR(30) NOT NULL,
    quantidade INT DEFAULT 1 
);

CREATE TABLE Emprestimo (
    id_emprestimo INT PRIMARY KEY AUTO_INCREMENT,
    id_leitor INT NOT NULL,
    id_livro INT NOT NULL, 
    data_emprestimo DATE NOT NULL,
    data_devolucao_prevista DATE NOT NULL,
    data_devolucao_realizada DATE NOT NULL,
    FOREIGN KEY (id_livro) REFERENCES livro(id_livro),
    FOREIGN KEY (id_leitor) REFERENCES leitor(id_leitor)
);