CREATE DATABASE integration_python;
USE integration_python;


CREATE TABLE users (
ID INT PRIMARY KEY AUTO_INCREMENT,
NOME VARCHAR(50) NOT NULL,
IDADE INT NOT NULL,
TELL VARCHAR(11) NOT NULL
);

INSERT INTO users (NOME, IDADE, TELL) VALUES 
('Thiago Vasques', 20, '11962754811'),
('Lucas Felipe', 78, '11943871522');
# ('Gabriel Cardoso', 19, '11962754755'),
# ('Valeria Bisco', 35, '11987457849');

SELECT * FROM users;
