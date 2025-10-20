def find_min_max(arr):
    """
    Знаходить мінімальний та максимальний елементи масиву
    за допомогою алгоритму 'розділяй і володарюй'.

    Args:
        arr (list): список чисел

    Returns:
        tuple: (мінімум, максимум)
    """
    # Базовий випадок: один елемент
    if len(arr) == 1:
        return arr[0], arr[0]

    # Базовий випадок: два елементи
    if len(arr) == 2:
        return (arr[0], arr[1]) if arr[0] < arr[1] else (arr[1], arr[0])

    # Рекурсивне розбиття
    mid = len(arr) // 2
    left_min, left_max = find_min_max(arr[:mid])
    right_min, right_max = find_min_max(arr[mid:])

    # Об’єднання результатів
    overall_min = min(left_min, right_min)
    overall_max = max(left_max, right_max)

    return overall_min, overall_max


# 🔹 Тестування
if __name__ == "__main__":
    data = [3, 5, 1, 8, 2, 10, 6]
    mn, mx = find_min_max(data)
    print(f"Мінімум: {mn}, Максимум: {mx}")
