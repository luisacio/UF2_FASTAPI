def format_schema(response):
    return {"option":response[0]}

def list_format_schema(list_response):
    if len(list_response) > 1:
        result = [format_schema(response) for response in list_response]
    else:
        result = [format_schema(list_response)]
    return result
'''
def format_mix_schema(response):
    return {"option":response}
'''
def list_format_game_schema(list_response):
    #return [format_mix_schema(response) for response in list_response]
    keys = ["id_partida", "num_intents", "punt_actual", "part_abierta", "palabra", "fecha_ini","fecha_fin"]
    return [{key: value} for key, value in zip(keys, list_response)]

def list_format_user_schema(list_response):
    #return [format_mix_schema(response) for response in list_response]
    keys = ["nombre", "partidas_total", "partidas_ganadas", "punt_record"]
    return [{key: value} for key, value in zip(keys, list_response)]

'''
def format_schema(response):
    return {"option":response[0]}

def format_mix_schema(response):
    return {"option":response}


def list_format_schema(list_response):
    if len(list_response) > 1:
        str_set = any(not isinstance(element, str) for element in list_response)
        if str_set:
            result = [format_mix_schema(response) for response in list_response]
        else:
            result = [format_schema(response) for response in list_response]
    else:
        result = [format_schema(list_response)]
    return result
'''