def swap_min_max(numbers):
    """Меняет местами минимальный и максимальный элементы списка."""
    if len(numbers) == 0:
        print("Список пуст. Нечего менять.")
        return numbers
    elif len(numbers) == 1:
        print("Список состоит из одного элемента. Нечего менять.")
        return numbers

    # Фильтруем нечисловые значения
    filtered_numbers = []
    for num in numbers:
        try:
            filtered_numbers.append(float(num))  # Пробуем привести к числу
        except ValueError:
            print(f"Значение '{num}' не является числом и будет проигнорировано.")

    if len(filtered_numbers) == 0:
        print("После фильтрации не осталось числовых значений.")
        return []

    min_value = min(filtered_numbers)
    max_value = max(filtered_numbers)

    # Проверяем, одинаковы ли минимальный и максимальный элементы
    if min_value == max_value:
        print("Максимальный и минимальный элементы одинаковы, не нужно ничего менять.")
        return filtered_numbers

    # Находим индексы первого минимального и максимального элементов
    min_index = filtered_numbers.index(min_value)
    max_index = filtered_numbers.index(max_value)

    # Меняем местами
    filtered_numbers[min_index], filtered_numbers[max_index] = filtered_numbers[max_index], filtered_numbers[min_index]

    return filtered_numbers

def main():
    try:
        user_input = input("Введите список чисел через запятую: ")
        # Преобразуем строку в список, разделив по запятой и убрав пробелы
        numbers = [x.strip() for x in user_input.split(",")]

        result = swap_min_max(numbers)
        print("Результат:", result)

    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
