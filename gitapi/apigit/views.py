import json

from django.shortcuts import render

from parser.parser import get_data

name = input('Введите имя пользователя Гитхаб: ')
url = ''.join(f"https://github.com/{name}?tab=repositories")
get_data(url)
with open(f'{name}.json', 'w', encoding="utf-8") as file:
    json.dump(get_data(url), file, indent=4, ensure_ascii=False)