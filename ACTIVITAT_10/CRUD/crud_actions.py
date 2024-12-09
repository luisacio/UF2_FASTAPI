from ACTIVITAT_10.BBDD import bbdd_management

def read_all_theme():
    cur_conn = bbdd_management.connect_to_bbdd()

    cur_conn[0].execute("""SELECT DISTINCT theme FROM public.game_words ORDER BY theme ASC  """)
    themes = cur_conn[0].fetchall()
    themes_dicc = [{"option": item[0]} for item in themes]
    cur_conn[0].close()
    cur_conn[1].close()

    return themes_dicc

def read_word(theme):
    cur_conn = bbdd_management.connect_to_bbdd()

    cur_conn[0].execute("""SELECT word FROM public.game_words 
                            WHERE theme = %s
                             ORDER BY RANDOM() LIMIT 1  """,(theme,))
    word_fetch =  cur_conn[0].fetchone()
    word = [{"option" : word_fetch[0]}]
    cur_conn[0].close()
    cur_conn[1].close()

    return word