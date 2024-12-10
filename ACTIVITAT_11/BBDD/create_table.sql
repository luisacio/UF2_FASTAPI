CREATE TABLE usuario (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(20)
);

CREATE TABLE usuario_puntuacion (
    id INT,
    punt_actual INT,
    partidas_total INT,
    partidas_win INT,
    punt_record INT,
    FOREIGN KEY (id) REFERENCES usuario(id)
);

CREATE TABLE game_words(

    word VARCHAR(20),
    theme VARCHAR(20),
);

CREATE TABLE info_render (
    code VARCHAR(20) PRIMARY KEY,
    render VARCHAR(100)
);
