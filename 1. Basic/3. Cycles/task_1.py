boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys) != len(girls):
    print('Кто-то может остаться без пары.')
else:
    boys.sort()
    girls.sort()
    pairs = zip(boys, girls)
    for pair in pairs:
        boy = pair[0]
        girl = pair[1]
        print(f'{boy} и {girl}')