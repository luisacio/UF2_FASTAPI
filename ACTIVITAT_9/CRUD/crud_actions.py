from ACTIVITAT_9.DB_CONNECT import bbdd_management

def read_all_users():
    cur_conn = bbdd_management.connect_to_bbdd()

    cur_conn[0].execute("""SELECT ID,NAME FROM public.users ORDER BY id ASC  """)
    users = cur_conn[0].fetchall()
    users_dicc = [{"id": item[0], "name": item[1]} for item in users]
    cur_conn[0].close()
    cur_conn[1].close()

    return users_dicc