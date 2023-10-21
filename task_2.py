salary = 1500               # зарплата
spend = 1550                # расходы в месяц
increase = 1.03             # рост цен в месяц

money_capital = 0   # счетчик
for i in range(10) :
    delta = - (salary - spend)  # долг за текущий месяц
    money_capital += delta      # требуемая фин. подушка к концу текущего месяцев
    spend = increase * spend    # расходы  на будущий месяц

print('На 10 месяцев фин. подушка должна быть не меньше', round(money_capital, 2), 'ед.')
print('это', round(money_capital/salary, 1), 'зарплаты')
