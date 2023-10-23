salary = 5000               # зарплата
money_capital = 20000       # финансовая подушка
spend = 6000                # расходы в месяц
increase = 0.05             # рост цен в месяц

i = 0       # счетчик
while money_capital > 0 :
    i += 1
    money_capital = money_capital + (salary - spend)    # подушка к концу i - го месяца
    spend += increase * spend    # расходы  на месяц (i + 1)

print('Фин. подушки хватит на', i - 1 , 'месяцев')
