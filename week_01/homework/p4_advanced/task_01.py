"""
ДЗ презентации 4, повышенный уровень, задача 1.
Время: 25–35 минут.

Тема: Decimal, ROUND_HALF_UP.

Условие:
    Запросите цену (строка, например "19.99"), количество
    и налоговую ставку в процентах. Вычислите итоговую стоимость
    с помощью Decimal, округлив до двух знаков по ROUND_HALF_UP.

Пример:
    In: 19.99
    In: 3
    In: 13
    Out: Overall: 67.77
"""
from decimal import Decimal, ROUND_HALF_UP


def total(price: str, qty: int, tax: str) -> str:
    # Decimal создаём из строк, а не из float,
    # иначе потеряем точность
    price_dec = Decimal(price)
    tax_rate = Decimal(tax) / 100      # 13 -> 0.13

    result = price_dec * qty * (1 + tax_rate)
    # округляем до копеек по правилу "половина — вверх"
    result = result.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    return f"Overall: {result}"


if __name__ == "__main__":
    assert total("19.99", 3, "13") == "Overall: 67.77"
    assert total("100", 1, "0") == "Overall: 100.00"
    print("task_01 (p4 advanced): тесты пройдены")
