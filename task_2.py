salary = 5000               # зарплата
spend = 6000                # расходы в месяц
months = 10                 # сколько месяцев без долгов
increase = 0.03             # рост цен в месяц

money_capital = 0   # счетчик
for i in range(months) :
    delta = - (salary - spend)  # долг за текущий месяц
    money_capital += delta      # требуемая фин. подушка к концу текущего месяцев
    spend += increase * spend    # расходы  на будущий месяц

print('На', months, 'месяцев фин. подушка должна быть не меньше', round(money_capital, 2), 'ед.')
print('это', round(money_capital/salary, 1), 'зарплаты')
