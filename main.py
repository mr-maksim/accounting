from datetime import date
from application.salary import calculate_salary
from application.db.people import get_employees


def nowdate():
    return date.today()


if __name__ == '__main__':
    calculate_salary(nowdate())
    get_employees(nowdate())
