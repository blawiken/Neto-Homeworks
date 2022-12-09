stats = {
    'facebook': 55,
    'yandex': 120,
    'vk': 115,
    'google': 99,
    'email': 42,
    'ok': 98
}

name = max(stats)
count = max(stats.values(), key=lambda i: int(i))
print(f'Максимальный объем продаж: {name} - {count}')