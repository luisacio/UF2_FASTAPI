import pandas as pd
from ACTIVITAT_10.BBDD import bbdd_management

df = pd.read_csv("paraules_temàtica_penjat.csv")

cur_conn = bbdd_management.connect_to_bbdd()

for index,row in df.iterrows():

    word_theme_tuple = (row.WORD, row.THEME)
    cur_conn[0].execute("INSERT INTO public.game_words (word,theme) values(%s,%s)",word_theme_tuple)
    print(word_theme_tuple)

cur_conn[1].commit()
cur_conn[0].close()
cur_conn[1].close()