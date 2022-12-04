salary = int(input("Какая у вас зарплата:"))
expenses = int(input("Какие у вас расходы:"))
month = int(input("Сколько месяцев вам нужно прожить:"))
percent = int(input("На сколько % растут расходы:"))
credit = expenses - salary
i = 1
while i <= month - 1:
  credit += expenses * (1 + percent / 100) ** i - salary
  i += 1
print(f"Необходимо взять в долг {format(credit,'.2f')} рублей")
