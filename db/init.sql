use user;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL
);

INSERT INTO users (username, email) VALUES ('Jean Costa', 'jean.costa4@fatec.sp.gov.br');
INSERT INTO users (username, email) VALUES ('Fatec SJC', 'fatecsjc@fatec.sp.gov.br');
