# импортируем, что понадобится
import json
from pprint import pprint


# функция считает сумму произведений значений словарей по двум ключам
def task():
    with open('input.json', 'r') as f:
        data = json.load(f)
        pprint(data)  # выгрузили список словарей

    SUM = 0     # счетчик
    for dict_ in data:
        score, weight = dict_.values()      # берем значения из словаря
        SUM += score * weight               # перемножаем, складываем
    print('\n Искомая сумма равна', round(SUM, 3))

task()
