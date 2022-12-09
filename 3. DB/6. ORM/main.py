import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
from models import *


username = ''
password = ''
name_db = ''
local = 'localhost'
port = '5432'
type_db = 'postgresql'

DSN = f'{type_db}://{username}:{password}@{local}:{port}/{name_db}'
engine = sq.create_engine(DSN)

# Создание таблиц
Base.metadata.create_all(engine)

# Сессия
Session = sessionmaker(bind=engine)
session = Session()

# Создание объектов
#publisher1 = Publisher(name='New school')
#publisher2 = Publisher(name='Old town')
#session.add_all([publisher1, publisher2])
#book1 = Book(title='New Age', id_publisher=1)
#book2 = Book(title='Total War', id_publisher=1) 
#book3 = Book(title='Argent Down', id_publisher=1)
#shop1 = Shop(name='Great Shop')
#shop2 = Shop(name='Amazing Shop')
#stock1 = Stock(id_book=1, id_shop=1, count=40)
#stock2 = Stock(id_book=2, id_shop=1, count=20)
#stock3 = Stock(id_book=3, id_shop=1, count=10)
#sale1 = Sale(price=1000, date_sale='22.10.2010', id_stock=1, count=40)
#sale2 = Sale(price=500, date_sale='23.09.2010', id_stock=2, count=40)
#session.add_all([sale2])
#session.commit()

# Запрос
if __name__ == '__main__':
    find_publisher_id = input('Введите ID издателя: ')
    
    q = session.query(Publisher).filter(Publisher.id == int(find_publisher_id)).all()

    # Перебираем книги
    for s in q:
        for book in s.books:
            book_name = book.title
            #print(book_name)
            
            q_stock = session.query(Stock).filter(Stock.id_book == book.id).all()

            for stock in q_stock:
                shop_name = stock.shop.name
                #print(shop_name)

                q_sale = session.query(Sale).filter(Sale.id_stock == stock.id).all()
                for sale in q_sale:
                    price = sale.price
                    date = sale.date_sale
                    print(f'{book_name} | {shop_name} | {price} | {date}')


    session.close()