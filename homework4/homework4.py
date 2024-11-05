def main():
    numbers = []  # Создаем пустой список для хранения чисел

    while True:
        user_input = input("Введите число (или 'end' для завершения): ")

        if user_input.lower() == 'end':
            break  # Завершаем цикл, если введено 'end'

        try:
            number = float(user_input)  # Пробуем преобразовать ввод в число
            numbers.append(number)  # Добавляем число в список
        except ValueError:
            print("Ошибка: Ввод должен содержать только числа. Пожалуйста, введите корректные значения.")

    # Подсчет четных и нечетных чисел
    even_count = sum(1 for num in numbers if num % 2 == 0)
    odd_count = sum(1 for num in numbers if num % 2 != 0)

    print(f"Количество четных чисел: {even_count}")
    print(f"Количество нечетных чисел: {odd_count}")

# Запуск основной функции
if __name__ == "__main__":
    main()
