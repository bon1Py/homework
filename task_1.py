salary = 1500               # зарплата
money_capital = 3 * salary  # финансовая подушка
spend = 1550                # расходы в месяц
increase = 1.05             # рост цен в месяц

i = 0       # счетчик
while money_capital > 0 :
    i += 1
    budget = salary + money_capital - spend  # бюджет к концу i-го месяца
    money_capital = money_capital + (salary - spend)    # подушка к концу i - го месяца
    spend = increase * spend    # расходы  на месяц (i + 1)

print('Фин. подушки хватит на', i - 1 , 'месяцев')
