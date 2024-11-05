def create_squares_list(a, b):
    # Проверка на вещественные числа
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Оба значения должны быть вещественными числами.")
    
    # Определяем границы
    start = int(min(a, b))
    end = int(max(a, b))
    
    # Создаем список квадратов целых чисел
    squares_list = [i**2 for i in range(start, end + 1)]
    
    return squares_list

# Пример использования
try:
    a = float(input("Введите число a: "))
    b = float(input("Введите число b: "))
    
    result = create_squares_list(a, b)
    print("Список квадратов целых чисел между a и b:", result)
except ValueError:
    print("Ошибка: Ввод должен содержать только числа. Пожалуйста, введите корректные значения.")
