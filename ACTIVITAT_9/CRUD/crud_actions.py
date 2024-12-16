from ACTIVITAT_9.DB_CONNECT import bbdd_management

def read_users():
    cur_conn = bbdd_management.connect_to_bbdd()

    cur_conn[0].execute("""SELECT ID,NAME FROM public.users ORDER BY id ASC  """)
    users = cur_conn[0].fetchall()
    cur_conn[0].close()
    cur_conn[1].close()

    return users