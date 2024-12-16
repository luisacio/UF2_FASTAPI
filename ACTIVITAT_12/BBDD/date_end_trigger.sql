CREATE OR REPLACE FUNCTION update_data_end()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.open_game = FALSE THEN
        NEW.data_end = CURRENT_TIMESTAMP;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_end
BEFORE UPDATE ON user_score
FOR EACH ROW
EXECUTE FUNCTION update_data2();
