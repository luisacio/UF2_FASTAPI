def word_theme_schema(word_theme):
    return {"option":word_theme[0]}

def words_themes_schema(list_words_themes):
    if len(list_words_themes) > 1:
        result = [word_theme_schema(word_theme) for word_theme in list_words_themes]
    else:
        result = [word_theme_schema(list_words_themes)]
    return result