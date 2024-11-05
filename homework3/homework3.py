def main():
    numbers = []  # Создаем пустой список для хранения чисел

    while True:
        user_input = input("Введите число (или 'end' для завершения): ")

        if user_input.lower() == 'end':
            break  # Завершаем цикл, если введено 'end'

        try:
            number = float(user_input)  # Пробуем преобразовать ввод в число
            if number % 2 != 0:  # Проверяем, является ли число нечетным
                numbers.append(number)  # Добавляем нечетное число в список
        except ValueError:
            print("Ошибка: Ввод должен содержать только числа. Пожалуйста, введите корректные значения.")

    print("Нечетные числа:", numbers)

# Запуск основной функции
if __name__ == "__main__":
    main()
