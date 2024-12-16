CREATE TABLE usuario (
    nombre VARCHAR(20),
    partidas_total INT,
    partidas_ganadas INT,
    punt_record INT
);

CREATE TABLE usuario_puntuacion (
    id_partida INT PRIMARY KEY,
    num_intents INT,
    punt_actual INT,
    part_abierta BOOLEAN,
    palabra VARCHAR(20),
    fecha_ini TIMESTAMP DEFAULT CURRENT_DATE,
    fecha_fin TIMESTAMP
);

CREATE TABLE game_words(
    word VARCHAR(20),
    theme VARCHAR(20)
);

CREATE TABLE info_render (
    code VARCHAR(20) PRIMARY KEY,
    render VARCHAR(100)
);
