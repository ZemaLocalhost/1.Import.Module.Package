from application import salary
from application.db import people
from datetime import datetime

if __name__ == '__main__':
    print('Вызываем функции по расчету зарплаты и получанию данных простого люда')
    salary.calculate_salary()
    people.get_employees()
    today = datetime.today()
    print(f'На дворе сегодня {today}')
