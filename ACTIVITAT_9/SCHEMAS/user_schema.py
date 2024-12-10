def user_schema(user):
    return {"id":user[0],
            "name":user[1]}

def users_schema(list_users):
    return [user_schema(user) for user in list_users]