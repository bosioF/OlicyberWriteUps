CREATE TABLE users (
    username VARCHAR(36) NOT NULL,
    password VARCHAR(36) NOT NULL,
    is_admin BOOLEAN DEFAULT(FALSE),
    PRIMARY KEY (username)
);

CREATE TABLE entries(
    id VARCHAR(36) NOT NULL,
    owner VARCHAR(36) NOT NULL,
    address TEXT NOT NULL,
    image TEXT,
    PRIMARY KEY (id),
    FOREIGN KEY (owner) REFERENCES users(username)
);
