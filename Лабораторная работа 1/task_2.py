# Задача - рассчитать, сколько одинаковых книг можно поместить
# на дискету, и вывести результат на экран

# Исходные данные
storage = 1.44 * 1024 * 1024    # 1.44 Мб в байт
page_count = 100                # страниц в одной книге
str_count = 50                  # строк на странице
sumbols_count = 25              # символов в строке
sumbol_weight = 4               # вес одного символа (байт)

# Расчет
book_weight = page_count * sumbols_count * sumbols_count * sumbol_weight    # вес книги (байт)
book_count = storage // book_weight
other = storage % book_weight

print('На дискете поместится ', book_count, ' книг')
print('Остаток памяти - ', round(other), 'байт')
