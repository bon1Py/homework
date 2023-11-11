# импортируем, что понадобится
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


# функция переводит csv в json
def task() -> None:
    with open(INPUT_FILENAME, 'r') as f_read:
        lines = [line for line in csv.DictReader(f_read)]

    with open(OUTPUT_FILENAME, 'w') as f_write:
        for line in lines:
            sequence = [json.dumps(line, indent=4), '\n']
            f_write.writelines(sequence)


# проверка
task()

with open(OUTPUT_FILENAME) as output_f:
    for line in output_f:
        print(line, end="")
