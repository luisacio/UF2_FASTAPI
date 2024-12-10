import json

# Lista de listas
lista_de_listas = [
    [1, "Luis", "García"],
    [2, "Maria", "Lopez"],
    [3, "Juan", "Martinez"]
]

# Transformar la lista de listas en una lista de diccionarios
lista_de_diccionarios = [{"id": item[0], "name": item[1], "surname": item[2]} for item in lista_de_listas]

# Convertir la lista de diccionarios a formato JSON
json_data = json.dumps(lista_de_diccionarios, indent=3)

# Imprimir el resultado en formato JSON
print(json_data)


lista = [
  [
    1,
    "Luis"
  ],
  [
    2,
    "Laura"
  ],
  [
    3,
    "Victor"
  ],
  [
    4,
    "Snake"
  ],
  [
    5,
    "Pepe"
  ]
]


final_dicc = {}
for l in lista:
    #final_dicc = dict(l)
    print(l)
print(lista)