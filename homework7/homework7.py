def cyclic_shift_right(numbers):
    """Циклически сдвигает элементы списка вправо на 1."""
    if len(numbers) == 0:
        print("Список пуст. Нечего сдвигать.")
        return numbers
    elif len(numbers) == 1:
        print("Список состоит из одного элемента. Нечего сдвигать.")
        return numbers

    # Сдвигаем элементы вправо
    last_element = numbers[-1]
    for i in range(len(numbers) - 1, 0, -1):
        numbers[i] = numbers[i - 1]
    numbers[0] = last_element

    return numbers

def main():
    try:
        user_input = input("Введите список чисел через запятую: ")
        # Преобразуем строку в список, разделив по запятой и убрав пробелы
        numbers = [x.strip() for x in user_input.split(",")]

        # Проверка на корректность чисел
        for num in numbers:
            try:
                float(num)  # Пробуем привести к числу
            except ValueError:
                print(f"Ошибка: значение '{num}' не является числом и будет проигнорировано.")
                numbers.remove(num)

        # Если после фильтрации остались числа, выполняем сдвиг
        if numbers:
            result = cyclic_shift_right(numbers)
            print("Результат:", result)
        else:
            print("После фильтрации не осталось числовых значений.")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()

