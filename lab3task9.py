salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

for fund in range(1, months + 1):
    fund = (spend - salary)
    spend = spend * (increase + 1)
    need_money += fund

print(round(need_money))
