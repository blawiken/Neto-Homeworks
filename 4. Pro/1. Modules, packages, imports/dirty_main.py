from application.salary import *
from application.db.people import *


def main():
    print("dirty_main.py")
    calculate_salary()
    get_employees()


if __name__ == "__main__":
    main()