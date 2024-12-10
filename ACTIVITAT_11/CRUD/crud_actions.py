from ACTIVITAT_11.BBDD import bbdd_management

def get_front_text(front_text):
    cur_conn = bbdd_management.connect_to_bbdd()

    cur_conn[0].execute("""SELECT render FROM public.info_render 
                            WHERE code = %s
                             ORDER BY RANDOM() LIMIT 1  """,(front_text,))
    render_fetch =  cur_conn[0].fetchone()
    render = [{"render" : render_fetch[0]}]
    cur_conn[0].close()
    cur_conn[1].close()

    return render

def get_tries_word(id_user):
    cur_conn = bbdd_management.connect_to_bbdd()

    cur_conn[0].execute("""SELECT render FROM public.info_render 
                                WHERE code = %s
                                 ORDER BY RANDOM() LIMIT 1  """, (front_text,))
    render_fetch = cur_conn[0].fetchone()
    render = [{"render": render_fetch[0]}]
    cur_conn[0].close()
    cur_conn[1].close()

    return

def post_tries_word(id_user):
    cur_conn = bbdd_management.connect_to_bbdd()

    cur_conn[0].execute("""SELECT render FROM public.info_render 
                                WHERE code = %s
                                 ORDER BY RANDOM() LIMIT 1  """, (front_text,))
    render_fetch = cur_conn[0].fetchone()
    render = [{"render": render_fetch[0]}]
    cur_conn[0].close()
    cur_conn[1].close()

    return