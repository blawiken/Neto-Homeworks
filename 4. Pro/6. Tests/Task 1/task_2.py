def get_uniqs(ids: dict):
    uniqs = []
    for id in ids.values():
        for num in id:
            if num not in uniqs:
                uniqs.append(num)
    return uniqs