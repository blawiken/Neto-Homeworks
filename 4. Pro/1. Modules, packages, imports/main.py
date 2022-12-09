from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import date
from aiogram import __version__ as aiogram_version


def main():
    print('Сегодняшняя дата:', date.today())
    print('Актуальная версия Aiogram:', aiogram_version)
    calculate_salary()
    get_employees()


if __name__ == "__main__":
    main()