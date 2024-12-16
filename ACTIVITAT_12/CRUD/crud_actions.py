from ACTIVITAT_12.BBDD import bbdd_management

#------------------------TAULA GAME_WORDS-------------------------#
#SELECT per mostrar tots els temes
def select_theme():
    cur_conn = bbdd_management.connect_to_bbdd()

    cur_conn[0].execute("""SELECT DISTINCT UPPER(theme) as theme FROM public.game_word ORDER BY theme ASC  """)
    themes = cur_conn[0].fetchall()
    cur_conn[0].close()
    cur_conn[1].close()


    return themes

#SELECT per mostrar paraula segons tematica
def select_word(theme):
    cur_conn = bbdd_management.connect_to_bbdd()

    cur_conn[0].execute("""SELECT UPPER(word) as word FROM public.game_word
                            WHERE theme = %s
                             ORDER BY RANDOM() LIMIT 1  """,(theme,))
    word_fetch =  cur_conn[0].fetchone()
    cur_conn[0].close()
    cur_conn[1].close()

    return word_fetch

#INSERT per crear paraula
def insert_word(game_word):
    cur_conn = bbdd_management.connect_to_bbdd()

    cur_conn[0].execute("""INSERT INTO public.game_word (theme,word)
                            VALUES (%s,%s)""",(game_word.theme,game_word.word))
    cur_conn[1].commit()
    cur_conn[0].close()
    cur_conn[1].close()

#UPDATE per modificar paraula
def update_word(game_word):
    cur_conn = bbdd_management.connect_to_bbdd()

    cur_conn[0].execute("""UPDATE public.game_word
                            SET word = %s
                            WHERE theme = %s
                            AND word = %s""",(game_word.new_word,game_word.theme,game_word.word))
    cur_conn[1].commit()
    cur_conn[0].close()
    cur_conn[1].close()

#DELETE per esborrar paraula
def delete_word(game_word):
    cur_conn = bbdd_management.connect_to_bbdd()

    cur_conn[0].execute("""DELETE FROM public.game_word
                                WHERE theme = %s
                                AND word = %s""", (game_word.theme, game_word.word))
    cur_conn[1].commit()
    cur_conn[0].close()
    cur_conn[1].close()

#------------------------TAULA INFO_RENDER-------------------------#
#SELECT per mostrar renders del jocs segon parametre
def select_render(render_code):
    cur_conn = bbdd_management.connect_to_bbdd()

    cur_conn[0].execute("""SELECT render FROM public.code_render 
                            WHERE code = %s""",(render_code,))
    render_fetch =  cur_conn[0].fetchone()
    cur_conn[0].close()
    cur_conn[1].close()

    return render_fetch

#INSERT render
def insert_render(code_render):
    cur_conn = bbdd_management.connect_to_bbdd()

    cur_conn[0].execute("""INSERT INTO public.code_render (code,render)
                            VALUES (%s,%s)""",(code_render.code,code_render.render))
    cur_conn[1].commit()
    cur_conn[0].close()
    cur_conn[1].close()

#UPDATE render
def update_render(code_render):
    cur_conn = bbdd_management.connect_to_bbdd()

    cur_conn[0].execute("""UPDATE public.code_render
                            SET render = %s
                            WHERE code = %s""",(code_render.render,code_render.code))
    cur_conn[1].commit()
    cur_conn[0].close()
    cur_conn[1].close()

#DELETE render
def delete_render(code_render):
    cur_conn = bbdd_management.connect_to_bbdd()

    cur_conn[0].execute("""DELETE FROM public.code_render
                            WHERE code = %s""",(code_render.code,))
    cur_conn[1].commit()
    cur_conn[0].close()
    cur_conn[1].close()

#------------------------TAULA USUARIO-------------------------#
#SELECT per mostrar dades del usuari
def select_user(user):
    cur_conn = bbdd_management.connect_to_bbdd()

    cur_conn[0].execute("""SELECT name ,
                            game_total ,
                            game_win ,
                            score_record FROM public.users
                            WHERE name = %s
                            """, (user,))
    part_fetch = cur_conn[0].fetchone()
    cur_conn[0].close()
    cur_conn[1].close()

    return part_fetch

#INSERT per crear usuari
def insert_user(user):
    cur_conn = bbdd_management.connect_to_bbdd()

    cur_conn[0].execute("""INSERT INTO public.users (
                            name ,
                            game_total ,
                            game_win ,
                            score_record)
                            VALUES (%s,%s,%s,%s)""", (user.name,
                                                            user.game_total,
                                                            user.game_win,
                                                            user.score_record))
    cur_conn[1].commit()
    cur_conn[0].close()
    cur_conn[1].close()

#UPDATE usuari
def update_user(user):
    cur_conn = bbdd_management.connect_to_bbdd()

    cur_conn[0].execute("""UPDATE public.users 
                            SET game_total = %s,
                            game_win = %s,
                            score_record = %s
                            WHERE name = %s""", (user.game_total,
                                                user.game_win,
                                                user.score_record,
                                                user.name))
    cur_conn[1].commit()
    cur_conn[0].close()
    cur_conn[1].close()

#DELETE usuari
def delete_user(user):
    cur_conn = bbdd_management.connect_to_bbdd()

    cur_conn[0].execute("""DELETE FROM public.users WHERE name = %s""", (user.name,))
    cur_conn[1].commit()
    cur_conn[0].close()
    cur_conn[1].close()

#------------------------TAULA USUARIO_PUNTUACION-------------------------#
#SELECT per mostrar dades de la partida
def select_user_score(id_game):
    cur_conn = bbdd_management.connect_to_bbdd()

    cur_conn[0].execute("""SELECT id_game ,
                            num_try ,
                            current_score ,
                            open_game ,
                            word ,
                            TO_CHAR(date_ini,'DD/MM/YYYY HH:MI:SS') AS date_ini,
                            TO_CHAR(date_end,'DD/MM/YYYY HH:MI:SS') AS date_end FROM public.user_score
                            WHERE id_game = %s
                            """, (id_game,))
    part_fetch = cur_conn[0].fetchone()
    cur_conn[0].close()
    cur_conn[1].close()

    return part_fetch

#INSERT per crear partida
#Les dates de inici i final s´encarrega la bbdd
def insert_user_score(user_score):
    cur_conn = bbdd_management.connect_to_bbdd()

    cur_conn[0].execute("""INSERT INTO public.user_score (
                            id_game ,
                            num_try ,
                            current_score ,
                            open_game ,
                            word)
                            VALUES (%s,%s,%s,%s,%s)""", (user_score.id_game,
                                                            user_score.num_try,
                                                            user_score.current_score,
                                                            user_score.open_game,
                                                            user_score.word))
    cur_conn[1].commit()
    cur_conn[0].close()
    cur_conn[1].close()

#UPDATE per guardar intents de la partida
#Les dates de inici i final s´encarrega la bbdd
#La suma de intents s´encarrega la bbdd
def update_user_score(user_score):
    cur_conn = bbdd_management.connect_to_bbdd()

    cur_conn[0].execute("""UPDATE public.user_score
                            SET num_try = num_try + 1,
                                current_score = %s,
                                open_game = %s
                            WHERE id_game = %s
                            """, (user_score.current_score,
                                  user_score.open_game,
                                  user_score.id_game
                                  ))
    cur_conn[1].commit()
    cur_conn[0].close()
    cur_conn[1].close()

#DELETE partida
def delete_user_score(user_score):
    cur_conn = bbdd_management.connect_to_bbdd()

    cur_conn[0].execute("""DELETE FROM public.user_score WHERE id_game = %s""",(user_score.id_game,))
    cur_conn[1].commit()
    cur_conn[0].close()
    cur_conn[1].close()