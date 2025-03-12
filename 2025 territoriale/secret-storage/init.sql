ALTER DATABASE mariadb CHARACTER SET utf8 COLLATE utf8_bin;

CREATE TABLE users (
    id INT AUTO_INCREMENT,
    username TEXT NOT NULL UNIQUE,
    PRIMARY KEY (id)
);

CREATE TABLE entries(
    id INT AUTO_INCREMENT,
    owner INT NOT NULL,
    name TEXT NOT NULL,
    secret TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT(NOW()),
    PRIMARY KEY (id),
    FOREIGN KEY (owner) REFERENCES users(id)
);