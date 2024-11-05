import random

def generate_random_list(size, lower_bound, upper_bound):
    """Генерирует список случайных чисел заданного размера и диапазона."""
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]

def compare_elements(numbers):
    """Сравнивает элементы списка и выводит те, которые больше предыдущего."""
    if not numbers:
        print("Список пуст.")
        return

    print("Исходный список:", numbers)
    
    last_element = numbers[-1]  # Сохраняем последний элемент для сравнения с нулем
    result = []

    for i in range(len(numbers)):
        if numbers[i] == 0:
            # Сравниваем с последним элементом
            if last_element > 0:
                result.append(last_element)
        elif i > 0 and numbers[i] > numbers[i - 1]:
            result.append(numbers[i])

    if result:
        print("Элементы, которые больше предыдущего:", result)
    else:
        print("Нет элементов, которые больше предыдущего.")

def main():
    try:
        # Генерируем список случайных чисел
        size = int(input("Введите размер списка: "))
        lower_bound = int(input("Введите нижнюю границу (включительно): "))
        upper_bound = int(input("Введите верхнюю границу (включительно): "))

        if size <= 0 or lower_bound > upper_bound:
            raise ValueError("Некорректные параметры для генерации списка.")

        random_list = generate_random_list(size, lower_bound, upper_bound)
        compare_elements(random_list)

    except ValueError as e:
        print(f"Ошибка ввода: {e}")

if __name__ == "__main__":
    main()
