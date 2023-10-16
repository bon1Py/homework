# Исходный список
numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
print('Исходный список', numbers)

# Нашли None, поменяли на 0
numbers = [(0 if x is None else x) for x in numbers]
print('Новый список   ', numbers)

# Меняем на среднее арифметическое
mean_num = round(sum(numbers)/len(numbers), 1)  # среднее
numbers = [(mean_num if x == 0 else x) for x in numbers]
print('Итоговый список', numbers)
