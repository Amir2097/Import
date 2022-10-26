from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
import pyshorteners

def reduction_url(full_url):
    '''Простая библиотека API-оболочки для сокращения URL-адресов'''
    s = pyshorteners.Shortener()
    print('Сокращенная ссылка - ', s.tinyurl.short(full_url))



if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(datetime.now())
    reduction_url('https://netology.ru/profile/program/adpy-62/lessons/216275/lesson_items/1144291')


