"""
ДЗ презентации 5, повышенный уровень, задача 1.
Время: 25–35 минут.

Тема: дробный рюкзак.

Условие:
    items — список кортежей (weight, value).
    Верните максимальную суммарную стоимость.

Пример:
    capacity = 50
    items = [(10, 60), (20, 100), (30, 120)]
    Ответ: 240.0
"""


def fractional_knapsack(capacity: float, items: list) -> float:
    # считаем, сколько стоит одна единица веса каждого предмета
    by_price = []
    for weight, value in items:
        price_per_kg = value / weight
        by_price.append((price_per_kg, weight, value))

    # жадно: сначала берём самые выгодные предметы
    by_price.sort(reverse=True)

    total_value = 0.0
    space_left = capacity

    for price_per_kg, weight, value in by_price:
        if space_left <= 0:
            break

        if weight <= space_left:
            # кладём предмет целиком
            total_value = total_value + value
            space_left = space_left - weight
        else:
            # кладём только часть, которая помещается
            total_value = total_value + price_per_kg * space_left
            space_left = 0

    return total_value


if __name__ == "__main__":
    items = [(10, 60), (20, 100), (30, 120)]
    assert abs(fractional_knapsack(50, items) - 240.0) < 1e-9
    assert fractional_knapsack(0, items) == 0.0
    print("task_01 (p5 advanced): тесты пройдены")
