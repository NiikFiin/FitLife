import time


WATER_PER_KG = 30  # константа для расчета нормы воды
ML_IN_L = 1000       # константа для перевода из мл в л


def greeting():
    """Приветствует и получает имя и возраст пользователя"""
    print('Привет, друг) Добро пожаловать в мир спорта! Давай познакомимся!')
    user_name = input('Как тебя зовут? ')
    while True:        # цикл для исключения ошибки
        try:
            user_age = int(input('Сколько тебе лет? '))
            break
        except ValueError:
            print('Ошибка :( Введите возраст')
    user_name = user_name.title()
    print(f'Приятно познакомиться, {user_name}, давай продолжим')
    return user_name, user_age


def get_weight_height():
    """Возвращает рост и вес пользователя"""
    while True:
        try:
            user_weight = float(input('Введи свой вес в кг (например, 65): '))
            user_height = float(input(
                'Введи свой рост в м (например, 1.78): '
            ))
            break
        except ValueError:
            print('Ошибка :( Введите вес в кг и рост в м')
    return user_weight, user_height


def calculate_bmi(user_weight, user_height):
    """Расчитывает и возвращает ИМТ"""
    return round((user_weight / (user_height ** 2)), 1)


def give_rec_about_water(user_weight):
    """Расчитывает и возвращает норму воды в сутки"""
    return user_weight * WATER_PER_KG / ML_IN_L


def final_report(user_name, user_age, bmi, water_l):
    """Вывод главного отчета"""
    print('Формируем отчет', end='')
    for _ in range(3):
        print('>', end='', flush=True)
        time.sleep(0.2)
    print('Отчет готов!\n')
    time.sleep(1)
    print('=' * 60)
    line_1 = (
        f'Отчет для пользователя: {user_name} '
        f'(возраст: {user_age})'
    )
    line_2 = f'Твой индекс массы тела: {bmi:.1f}'
    line_3 = f'Рекомендуемая норма воды в день: {water_l:.1f}л в день'
    print(f'|{line_1:^58}|')
    print(f'|{line_2:^58}|')
    print(f'|{line_3:^58}|')
    print(f'|{"Будь здоров!":^58}|')
    print('=' * 60)


user_name, user_age = greeting()
user_weight, user_height = get_weight_height()
bmi = calculate_bmi(user_weight, user_height)
water_l = give_rec_about_water(user_weight)
final_report(user_name, user_age, bmi, water_l)
