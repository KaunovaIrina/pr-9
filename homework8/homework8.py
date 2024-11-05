import random

def generate_ticket():
    """Создает лотерейный билет."""
    return [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]

def get_user_choices(ticket):
    """Запрашивает у пользователя выбор чисел из каждой строки билета."""
    user_choices = []
    for i in range(len(ticket)):
        while True:
            try:
                choice = int(input(f"Выберите число из строки {i + 1} {ticket[i]}: "))
                if choice in ticket[i]:
                    user_choices.append(choice)
                    break
                else:
                    print("Ошибка: Выберите число из предложенных.")
            except ValueError:
                print("Ошибка: Пожалуйста, введите целое число.")
    return user_choices

def generate_random_choices(ticket):
    """Генерирует случайный выбор чисел из каждой строки билета."""
    return [random.choice(row) for row in ticket]

def compare_choices(user_choices, program_choices):
    """Сравнивает выборы пользователя и программы и возвращает статистику."""
    comparison = []
    for user_choice, program_choice in zip(user_choices, program_choices):
        comparison.append([user_choice, program_choice])
    return comparison

def main():
    ticket = generate_ticket()
    
    print("Добро пожаловать в лотерею!")
    
    # Получаем выбор пользователя
    user_choices = get_user_choices(ticket)
    
    # Генерируем случайный выбор программы
    program_choices = generate_random_choices(ticket)
    
    # Сравниваем выборы
    comparison = compare_choices(user_choices, program_choices)
    
    print("nСтатистика:")
    print("Ваши числа и числа программы:")
    for user_num, program_num in comparison:
        print(f"Вы: {user_num}, Программа: {program_num}")

if __name__ == "__main__":
    main()
