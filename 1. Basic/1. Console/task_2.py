profit = int(input('Введите заработную плату в месяц:'))
credit = int(input('Введите, какой процент(%) уходит на ипотеку:'))
expense = int(input('Введите, какой процент(%) уходит на жизнь:'))

credit_result = int(profit * credit / 100)
cash_savings = profit - credit_result - int(profit * expense / 100)

print('На ипотеку было потрачено:', credit_result * 12)
print('Было накоплено:', cash_savings * 12)