from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
    print("Выполнение функции calculate_salary из модуля salary.py:")
    calculate_salary()
    print("Выполнение функции get_employees из модуля people.py:")
    get_employees()
