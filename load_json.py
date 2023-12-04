import json

with open("data_movies.json", "r", encoding='utf8') as arquivo:
    a = json.load(arquivo)

print(a)

