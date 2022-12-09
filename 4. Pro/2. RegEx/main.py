import csv
import re


def main():
    with open('phonebook_raw.csv', encoding='utf8') as f:
        rows = csv.reader(f, delimiter=',')
        contacts_list = list(rows)

    for contact in contacts_list[1:]:
        # ФИО
        names = re.findall(r'\w+', contact[0])
        if len(names) > 1:
            for i, name in enumerate(names):
                contact[i] = name

        names = re.findall(r'\w+', contact[1])
        if len(names) > 1:
            for i, name in enumerate(names):
                contact[i + 1] = name

        # Телефон
        pattern = r'(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?'
        result = re.sub(pattern, r'+7(\2)\3-\4-\5\7\8\9', contact[5])
        contact[5] = result
        
    # Дубликаты
    new_list = []
    new_list.append(contacts_list[0])
    for c in contacts_list[1:]:
        first_name = c[0]
        last_name = c[1]

        for contact in contacts_list:
            new_fn = contact[0]
            new_ln = contact[1]

            if first_name == new_fn and last_name == new_ln:
                if c[2] == '':
                    c[2] = contact[2]
                if c[3] == '':
                    c[3] = contact[3]
                if c[4] == '':
                    c[4] = contact[4]
                if c[5] == '':
                    c[5] = contact[5]
                if c[6] == '':
                    c[6] = contact[6]

        # \o/
        while len(c) > 7:
            c.remove('')

        if c not in new_list:
            new_list.append(c)

    with open('phonebook.csv', 'w', encoding='utf8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(new_list)


if __name__ == '__main__':
    main()