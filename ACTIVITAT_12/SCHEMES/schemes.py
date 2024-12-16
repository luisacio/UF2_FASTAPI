#Schema para el render, les tematiques i la paraula
def format_schema(response):
    return {"option":response[0]}

#Funcio per esquematitzar llistes de renders
def list_format_schema(list_response):
    if len(list_response) > 1:
        result = [format_schema(response) for response in list_response]
    else:
        result = [format_schema(list_response)]
    return result

#Schema per la partida
def list_format_game_schema(list_response):
    keys = ["id_game", "num_try", "current_score", "open_game", "word", "date_ini","date_end"]
    return [{key: value} for key, value in zip(keys, list_response)]

#Schema per l´usuari
def list_format_user_schema(list_response):
    keys = ["name", "game_total", "game_win", "score_record"]
    return [{key: value} for key, value in zip(keys, list_response)]
