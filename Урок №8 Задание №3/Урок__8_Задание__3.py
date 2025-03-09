def min_boats_needed(m, n, weights):
    # Сортируем веса рыбаков
    weights.sort()
    
    left = 0  # Указатель на самого легкого рыбака
    right = n - 1  # Указатель на самого тяжелого рыбака
    boats = 0  # Счетчик лодок

    while left <= right:
        # Если самый легкий и самый тяжелый рыбак могут поместиться в одну лодку
        if weights[left] + weights[right] <= m:
            left += 1  # Убираем самого легкого
        # Убираем самого тяжелого
        right -= 1
        boats += 1  # Увеличиваем счетчик лодок

    return boats

def main():
    # Вводим максимальную массу, которую может выдержать одна лодка
    m = int(input("Введите максимальную массу, которую может выдержать одна лодка (m): "))
    
    # Вводим количество рыбаков
    n = int(input("Введите количество рыбаков (n): "))
    
    # Вводим веса рыбаков
    weights = []
    for _ in range(n):
        weight = int(input("Введите вес рыбака: "))
        weights.append(weight)

    # Вычисляем минимальное количество лодок
    result = min_boats_needed(m, n, weights)

    # Выводим результат
    print(result)

if __name__ == "__main__":
    main()