cook_book = [
    ['салат',
        [
            ['картофель', 100, 'гр.'],
            ['морковь', 50, 'гр.'],
            ['огурцы', 50, 'гр.'],
            ['горошек', 30, 'гр.'],
            ['майонез', 70, 'мл.'],
        ]
    ],
    ['пицца',
        [
            ['сыр', 50, 'гр.'],
            ['томаты', 50, 'гр.'],
            ['тесто', 100, 'гр.'],
            ['бекон', 30, 'гр.'],
            ['колбаса', 30, 'гр.'],
            ['грибы', 20, 'гр.'],
        ]
    ],
    ['фруктовый десерт',
        [
            ['хурма', 60, 'гр.'],
            ['киви', 60, 'гр.'],
            ['творог', 60, 'гр.'],
            ['сахар', 10, 'гр.'],
            ['мед', 50, 'мл.'],
        ]
    ],
]
person = 5

for dish in cook_book:
    dish_name = dish[0]
    ingredients = dish[1]
    print(f'{dish_name.title()}:')

    for ingredient in ingredients:
        ingredient_name = ingredient[0]
        total_count = ingredient[1] * person
        unit = ingredient[2]
        print(f'{ingredient_name}, {total_count}{unit}')
    print('')