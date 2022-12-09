ids = {
    'user1': [213, 213, 213, 15, 213],
    'user2': [54, 54, 119, 119, 119],
    'user3': [213, 98, 98, 35]
    }
uniqs = []

for id in ids.values():
    for num in id:
        if num not in uniqs:
            uniqs.append(num)
print(uniqs)

# uniqs = set()
# for id in ids.values():
#     uniqs.update(id)
# print(uniqs)