queries = [
    'смотреть',
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
    'смотреть новинки кино боевики комедии ужасы документальное',
    'необходимо срочно придумать предложение для поиска в яндексе из 11 слов'
]
data = {}

for q in queries:
    words_num = len(q.split())
    if words_num not in data:
        data.update(
            {words_num: 1}
        )
    else:
        data[words_num] += 1

for words_num, count in data.items():
    percent = int(100 / (len(queries) / count))
    if words_num == 1:
        word = 'слова'
    else:
        word = 'слов'
    print(f'Поисковых запросов из {words_num} {word} - {percent}%')