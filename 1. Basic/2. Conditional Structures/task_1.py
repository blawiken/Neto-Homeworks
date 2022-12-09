print('Доступные регионы: \
    \nДальный восток, Ближний Восток, Дальний Запад, Ближний Запад.\n')

region = input('Введите регион: ').lower()

if region == 'дальний восток':
    base_rate = 2
else:
    if region == 'ближний восток':
        base_rate = 3
    elif region == 'дальний запад':
        base_rate = 4
    elif region == 'ближний запад':
        base_rate = 5
    
    kids = input('Детей больше 3? Y/N ').lower()
    has_project = input('Зарплатный проект в этом банке? Y/N ').lower()
    insurance_reg = input('Планируете оформление страхования? Y/N ').lower()

    if kids == 'y':
        base_rate -= 1
    if has_project == 'y':
        base_rate -= 0.5
    if insurance_reg == 'y':
        base_rate -= 1.5
print(f'Процентная ставка по кредиту: {base_rate}%')