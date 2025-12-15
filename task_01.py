# Стратегія обрання на кожному кроці двох кабелів з найменшою довжиною
# Додавання отриманого з'єднання до купи: щоб короткі кабелі додавалися частіше, а довгі — в кінці
# Оптимальна структура даних — міні-купа

import heapq

def min_cost_to_connect_cables(cables):
    # 1. Базова перевірка
    if len(cables) <= 1:
        return 0

    # 2. Копія списку для уникнення модифікації вхідних даних
    heap = cables.copy()
    
    # Перетворення копії у купу
    heapq.heapify(heap)

    total_cost = 0

    while len(heap) > 1:
        # Дістаємо два найменші кабелі
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)

        # Рахуємо витрати
        current_cost = first + second
        
        # Додаємо до загальних витрат
        total_cost += current_cost

        # Кладемо назад у купу
        heapq.heappush(heap, current_cost)

    return total_cost

# Перевірка
cables = [4, 3, 2, 6]

# Очікуваний порядок:
# 1. Беремо 2 і 3 -> сума 5. Витрати: 5. Купа: [4, 5, 6]
# 2. Беремо 4 і 5 -> сума 9. Витрати: 5 + 9 = 14. Купа: [6, 9]
# 3. Беремо 6 і 9 -> сума 15. Витрати: 14 + 15 = 29. Купа: [15]
# Результат: 29

print(f"Вхідні кабелі: {cables}")
result = min_cost_to_connect_cables(cables)
print(f"Мінімальні витрати: {result}")

