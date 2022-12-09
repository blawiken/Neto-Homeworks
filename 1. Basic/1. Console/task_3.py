# Task 1 code
length = int(input('Введите длину стороны квадрата:'))
symbol_count = length * 4

print('Периметр:', length * 4)
print('Площадь:', length ** 2)

length = int(input('Введите длину прямоугольника:'))
width = int(input('Введите ширину прямоугольника:'))

print('Периметр:', (length + width) * 2)
print('Площадь:', length * width)
symbol_count += length * width

# Task 3 code
symbol = input()
print(symbol * symbol_count)

# Task 2 code
profit = int(input('Введите заработную плату в месяц:'))
credit = int(input('Введите, какой процент(%) уходит на ипотеку:'))
expense = int(input('Введите, какой процент(%) уходит на жизнь:'))

credit_result = int(profit * credit / 100)
cash_savings = profit - credit_result - int(profit * expense / 100)

print('На ипотеку было потрачено:', credit_result * 12)
print('Было накоплено:', cash_savings * 12)