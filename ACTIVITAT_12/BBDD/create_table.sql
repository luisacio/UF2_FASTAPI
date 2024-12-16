--Creacio tablas
CREATE TABLE users (
    name VARCHAR(20),
    game_total INT,
    game_win INT,
    score_record INT
);

CREATE TABLE user_score (
    id_game INT PRIMARY KEY,
    num_try INT,
    current_score INT,
    open_game BOOLEAN,
    word VARCHAR(20),
    date_ini TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    date_end TIMESTAMP
);

CREATE TABLE game_word(
    word VARCHAR(20),
    theme VARCHAR(20)
);

CREATE TABLE code_render (
    code VARCHAR(20) PRIMARY KEY,
    render VARCHAR(100)
);

--Creacio funcio i trigger per informar la data i hora d inici i final
CREATE FUNCTION update_date_end()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.open_game = FALSE THEN
        NEW.date_end = CURRENT_TIMESTAMP;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_date_end
BEFORE UPDATE ON user_score
FOR EACH ROW
EXECUTE FUNCTION update_date_end();