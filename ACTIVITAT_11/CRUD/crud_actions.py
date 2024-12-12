from ACTIVITAT_11.BBDD import bbdd_management

#SELECT per mostrar tots els temes
def read_all_theme():
    cur_conn = bbdd_management.connect_to_bbdd()

    cur_conn[0].execute("""SELECT DISTINCT theme FROM public.game_words ORDER BY theme ASC  """)
    themes = cur_conn[0].fetchall()
    cur_conn[0].close()
    cur_conn[1].close()

    return themes

#SELECT per mostrar paraula segons tematica
def read_word(theme):
    cur_conn = bbdd_management.connect_to_bbdd()

    cur_conn[0].execute("""SELECT word FROM public.game_words 
                            WHERE theme = %s
                             ORDER BY RANDOM() LIMIT 1  """,(theme,))
    word_fetch =  cur_conn[0].fetchone()
    cur_conn[0].close()
    cur_conn[1].close()

    return word_fetch

#SELECT per mostrar renders del jocs segon parametre
def get_render(render_code):
    cur_conn = bbdd_management.connect_to_bbdd()

    cur_conn[0].execute("""SELECT render FROM public.info_render 
                            WHERE code = %s
                             ORDER BY RANDOM() LIMIT 1  """,(render_code,))
    render_fetch =  cur_conn[0].fetchone()
    cur_conn[0].close()
    cur_conn[1].close()

    return render_fetch

#UPDATE per guardar intents
def post_save_try(usuario_puntuacion):
    cur_conn = bbdd_management.connect_to_bbdd()

    cur_conn[0].execute("""UPDATE public.usuario_puntuacion
                            SET num_intents = num_intents + 1,
                                punt_actual = %s,
                                part_abierta = %s,
                                fecha_fin = %s
                            WHERE id_partida = %s
                            """, (usuario_puntuacion.punt_actual,
                                  usuario_puntuacion.part_abierta,
                                  usuario_puntuacion.fecha_fin,
                                  usuario_puntuacion.id_partida
                                  ))
    cur_conn[1].commit()
    cur_conn[0].close()
    cur_conn[1].close()

#INSERT per crear partida
def post_insert_game(usuario_puntuacion):
    cur_conn = bbdd_management.connect_to_bbdd()

    cur_conn[0].execute("""INSERT INTO public.usuario_puntuacion (
                            id_partida ,
                            num_intents ,
                            punt_actual ,
                            part_abierta ,
                            palabra)
                            VALUES (%s,%s,%s,%s,%s)""", (usuario_puntuacion.id_partida,
                                                            usuario_puntuacion.num_intents,
                                                            usuario_puntuacion.punt_actual,
                                                            usuario_puntuacion.part_abierta,
                                                            usuario_puntuacion.palabra))
    cur_conn[1].commit()
    cur_conn[0].close()
    cur_conn[1].close()

#INSERT per crear usuari
def post_insert_user(usuario):
    cur_conn = bbdd_management.connect_to_bbdd()

    cur_conn[0].execute("""INSERT INTO public.usuario (
                            nombre ,
                            partidas_total ,
                            partidas_ganadas ,
                            punt_record)
                            VALUES (%s,%s,%s,%s)""", (usuario.nombre,
                                                            usuario.partidas_total,
                                                            usuario.partidas_ganadas,
                                                            usuario.punt_record))
    cur_conn[1].commit()
    cur_conn[0].close()
    cur_conn[1].close()

#SELECT per mostrar dades de la partida
def get_game_data(id_partida):
    cur_conn = bbdd_management.connect_to_bbdd()

    cur_conn[0].execute("""SELECT id_partida ,
                            num_intents ,
                            punt_actual ,
                            part_abierta ,
                            palabra ,
                            TO_CHAR(fecha_ini,'DD/MM/YYYY HH:MI:SS') AS fecha_ini,
                            TO_CHAR(fecha_fin,'DD/MM/YYYY HH:MI:SS') AS fecha_fin FROM public.usuario_puntuacion
                            WHERE id_partida = %s
                            """, (id_partida,))
    part_fetch = cur_conn[0].fetchone()
    cur_conn[0].close()
    cur_conn[1].close()

    return part_fetch

#SELECT per mostrar dades del usuari
def get_game_user(user):
    cur_conn = bbdd_management.connect_to_bbdd()

    cur_conn[0].execute("""SELECT nombre ,
                            partidas_total ,
                            partidas_ganadas ,
                            punt_record FROM public.usuario
                            WHERE nombre = %s
                            """, (user,))
    part_fetch = cur_conn[0].fetchone()
    cur_conn[0].close()
    cur_conn[1].close()

    return part_fetch