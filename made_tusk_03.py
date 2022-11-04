user_input = input('Введите номер месяца: ')
month = int(user_input)
days31 = [1, 3, 5, 7, 8, 10, 12]
days30 = [4, 6, 9, 11]
days28 = [2]
if month in days31:
        print(31)
elif month in days30:
        print(30)
elif month in days28:
        print(28)
else: print('Вы ввели некорректный месяц')
