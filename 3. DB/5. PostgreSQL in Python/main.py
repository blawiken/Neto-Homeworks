import psycopg2


def create_db(cur):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS client(
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            email TEXT NOT NULL
        );
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phone(
            id SERIAL PRIMARY KEY,
            client_id INTEGER REFERENCES client(id),
            number INTEGER
        );
    """)


def add_client(cur, first_name, last_name, email, phones=None):
    cur.execute(f"""
        INSERT INTO client(first_name, last_name, email)
        VALUES ('{first_name}', '{last_name}', '{email}');
    """)
    cur.execute(f"""
        SELECT id FROM client WHERE first_name = '{first_name}' AND last_name = '{last_name}';
    """)
    client_id = cur.fetchall()
    client_id = str(client_id[0][0])
    cur.execute(f"""
        INSERT INTO phone(client_id, number)
        VALUES ('{client_id}', {phones});
    """)


def add_phone(cur, client_id, number):
    cur.execute(f"""
        INSERT INTO phone(client_id, number)
        VALUES ('{client_id}', '{number}');
    """)


def client_change(cur, client_id, first_name=None, last_name=None, email=None, phones=None):
    if first_name != None:
        cur.execute(f"""
            UPDATE client SET first_name = '{first_name}' WHERE id = {client_id};
        """)
    if last_name != None:
        cur.execute(f"""
            UPDATE client SET last_name = '{last_name}' WHERE id = {client_id};
        """)
    if email != None:
        cur.execute(f"""
            UPDATE client SET email = '{email}' WHERE id = {client_id};
        """)
    if phones != None:
        cur.execute(f"""
            UPDATE phone SET number = '{phones}' WHERE client_id = {client_id};
        """)


def phone_delete(cur, client_id, number):
    cur.execute(f"""
        DELETE FROM phone WHERE client_id = {client_id};
    """)


def client_delete(cur, client_id):
    cur.execute(f"""
        DELETE FROM phone WHERE client_id = {client_id};
    """)
    cur.execute(f"""
        DELETE FROM client WHERE id = {client_id};
    """)


def search_client(cur, first_name=None, last_name=None, email=None, phone=None):
    cur.execute(f"""
        SELECT * FROM client WHERE
        first_name = '{first_name}' \
        OR last_name = '{last_name}' \
        OR email = '{email}';
    """)
    users = cur.fetchall()
    user_id = users[0][0]
    user_name = users[0][1]
    user_last_name = users[0][2]
    user_email = users[0][3]

    cur.execute(f"""
        SELECT number FROM phone WHERE client_id = '{user_id}'
    """)
    numbers = cur.fetchall()
    for _ in users:
        print(f'ID: {user_id} | NAME: {user_name} | LAST_NAME: {user_last_name} | EMAIL: {user_email} | PHONES: {numbers}')


if __name__ == '__main__':
    with psycopg2.connect(database='netology_db', user='postgres',
        password='') as conn:
        with conn.cursor() as cur:
            create_db(cur)
            add_client(cur, 'Ivan', 'Selukov', 'email@mail.ru', '+123')
            add_phone(cur, 1, '5555')
            client_change(cur, 1, first_name="Oleg", phones='777')
            #phone_delete(cur, 2, '123')
            client_delete(cur, 2)
            search_client(cur, 'Oleg')

            conn.commit()