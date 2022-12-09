months = [
    'январь',
    'февраль',
    'март',
    'апрель',
    'май',
    'июнь',
    'июль',
    'август',
    'сентябрь',
    'октябрь',
    'ноябрь',
    'декабрь'
]
month = input('Введите месяц: ').lower()

if month not in months:
    print('Месяц указан неверно.')
else:
    day = int(input('Введите число: '))
    if day > 31 or day < 1:
        print('Число указанно неверно!')
    else:
        if month == 'декабрь':
            if day >= 22:
                zodiac = 'Козерог'
            else:
                zodiac = 'Стрелец'

        elif month == 'январь':
            if day >= 21:
                zodiac = 'Водолей'
            else:
                zodiac = 'Козерог'
        
        elif month == 'февраль':
            if day >= 20:
                zodiac = 'Рыбы'
            else:
                zodiac = 'Водолей'

        elif month == 'март':
            if day >= 21:
                zodiac = 'Овен'
            else:
                zodiac = 'Рыбы'

        elif month == 'апрель':
            if day >= 21:
                zodiac = 'Телец'
            else:
                zodiac = 'Овен'
        
        elif month == 'май':
            if day >= 21:
                zodiac = 'Близнецы'
            else:
                zodiac = 'Телец'
        
        elif month == 'июнь':
            if day >= 22:
                zodiac = 'Рак'
            else:
                zodiac = 'Близнецы'

        elif month == 'июль':
            if day >= 23:
                zodiac = 'Лев'
            else:
                zodiac = 'Рак'
        
        elif month == 'август':
            if day >= 24:
                zodiac = 'Дева'
            else:
                zodiac = 'Лев'

        elif month == 'сентябрь':
            if day >= 24:
                zodiac = 'Весы'
            else:
                zodiac = 'Дева'
        
        elif month == 'октябрь':
            if day >= 24:
                zodiac = 'Скорпион'
            else:
                zodiac = 'Весы'

        elif month == 'ноябрь':
            if day >= 23:
                zodiac = 'Стрелец'
            else:
                zodiac = 'Скорпион'
    
        print(f'Ваш знак зодиака: {zodiac}')