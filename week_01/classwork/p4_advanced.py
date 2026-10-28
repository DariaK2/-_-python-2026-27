"""
Презентация 4 — повышенный уровень.
Задачи уровня 3 (3.1–3.3, работа со строками и форматирование)
и уровня 4 (decimal и fractions).

Решения писать здесь. Тесты — в конце файла.
"""

from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction

# ============================================================
# Задача 3.1. Безопасный ввод числа
# ============================================================
# Условие:
#   Запросите у пользователя число. Если введено не число,
#   выведите сообщение об ошибке.
#   Используйте методы строк и преобразование типов.
#
# Пример:
#   In: 42
#   Out: OK: 42
#
#   In: abc
#   Out: Not a number


def safe_input(s: str) -> str:
    """Вернуть 'OK: <n>' или 'Not a number'."""
    # положительное число: все символы — цифры
    is_positive = s.isdigit()
    # отрицательное число: сначала минус, потом только цифры
    is_negative = s.startswith("-") and s[1:].isdigit()

    if is_positive or is_negative:
        n = int(s)
        return f"OK: {n}"
    else:
        return "Not a number"


# ============================================================
# Задача 3.2. Разбор строки
# ============================================================
# Условие:
#   Запросите строку вида "имя:возраст". Разделите её по символу :
#   и выведите приветствие с возрастом, увеличенным на 1.
#
# Пример:
#   In: Ivan:24
#   Out: Hello, Ivan! Next year you are 25.


def parse_name_age(s: str) -> str:
    """Вернуть приветствие с возрастом +1."""
    parts = s.split(":")  # "Ivan:24" -> ["Ivan", "24"]
    name = parts[0]
    age = int(parts[1])

    next_age = age + 1
    return f"Hello, {name}! Next year you are {next_age}."


# ============================================================
# Задача 3.3. Форматирование счёта
# ============================================================
# Условие:
#   Запросите название товара, цену за единицу и количество.
#   Выведите чек с выравниванием по правому краю и итоговой суммой.
#
# Пример:
#   In: apple
#   In: 15.5
#   In: 3
#   Out:
#     Product: apple
#     Cost: 15.50
#     Amount: 3
#     - - - - - - - - - - - - - - - - - - - -
#     Overall: 46.50


def format_receipt(product: str, cost: float, amount: int) -> str:
    """Вернуть строку чека."""
    overall = cost * amount

    # >10 — выровнять по правому краю в поле шириной 10 символов,
    # .2f — показать ровно два знака после точки
    line1 = f"Product: {product:>10}"
    line2 = f"Cost:    {cost:>10.2f}"
    line3 = f"Amount:  {amount:>10}"
    line4 = "- " * 20
    line5 = f"Overall: {overall:>10.2f}"

    # собираем строки чека через перенос строки
    receipt = line1 + "\n" + line2 + "\n" + line3 + "\n"
    receipt = receipt + line4 + "\n" + line5
    return receipt


# ============================================================
# Задача 4.1. Точный расчёт стоимости (Decimal)
# ============================================================
# Условие:
#   Запросите цену товара (строка, например "19.99"), количество
#   и налоговую ставку в процентах. Вычислите итоговую стоимость
#   с помощью Decimal, округлив до двух знаков по ROUND_HALF_UP.
#
# Пример:
#   In: 19.99
#   In: 3
#   In: 13
#   Out: Overall: 67.77


def exact_total(price: str, quantity: int, tax_percent: str) -> str:
    """Вернуть итоговую стоимость строкой с 2 знаками."""
    # Decimal создаём из строки, чтобы не было ошибок float
    price_dec = Decimal(price)
    tax = Decimal(tax_percent) / 100  # 13 % -> 0.13

    total = price_dec * quantity * (1 + tax)
    # округляем до копеек: 0.5 и больше — вверх
    total = total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    return str(total)


# ============================================================
# Задача 4.2. Сравнение float и Decimal
# ============================================================
# Условие:
#   Сложите 0.1 + 0.2 двумя способами: через float и через Decimal.
#   Выведите оба результата и проверьте, равны ли они 0.3.
#
# Пример:
#   float: 0.30000000000000004 -> False
#   Decimal: 0.3 -> True


def compare_float_decimal() -> tuple:
    """Вернуть (float_sum, float_eq, decimal_sum, decimal_eq)."""
    # float хранит числа в двоичном виде, поэтому 0.1 + 0.2
    # получается чуть больше 0.3
    float_sum = 0.1 + 0.2
    float_eq = float_sum == 0.3

    # Decimal считает в десятичной системе, как мы на бумаге
    decimal_sum = Decimal("0.1") + Decimal("0.2")
    decimal_eq = decimal_sum == Decimal("0.3")

    print(f"float: {float_sum} -> {float_eq}")
    print(f"Decimal: {decimal_sum} -> {decimal_eq}")

    return float_sum, float_eq, decimal_sum, decimal_eq


# ============================================================
# Задача 4.3. Сумма дробей (Fraction)
# ============================================================
# Условие:
#   Запросите две обыкновенные дроби в формате "числитель/знаменатель".
#   Сложите их с помощью Fraction и выведите результат в виде
#   несократимой дроби.
#
# Пример:
#   In: 1/3
#   In: 1/6
#   Out: 1/2


def sum_fractions(frac1: str, frac2: str) -> str:
    """Вернуть несократимую сумму дробей строкой."""
    # Fraction понимает строки вида "1/3" и сам сокращает дробь
    first = Fraction(frac1)
    second = Fraction(frac2)

    result = first + second
    # если знаменатель 1, str() вернёт просто "1"
    return str(result)


# ============================================================
# Задача 4.4. Точное деление счёта
# ============================================================
# Условие:
#   Счёт в ресторане составил 1234.56 руб. Его нужно разделить
#   на 7 человек поровну. Вычислите долю каждого с помощью Decimal
#   и округлите до копеек. Проверьте, что сумма долей не превышает
#   исходный счёт.
#
# Пример:
#   Account: 1234.56
#   Guests: 7
#   Share: 176.37
#   Sum: 1234.59 (over 0.03)
#
# Вопрос: как распределить «лишние» копейки, чтобы сумма долей
#   точно совпала со счётом?
# Ответ: округлить долю вниз (176.36), тогда сумма будет 1234.52,
#   и оставшиеся 4 копейки отдать по одной первым четырём гостям:
#   4 человека платят 176.37, а 3 человека — 176.36.


def split_bill(account: str, guests: int) -> dict:
    """Вернуть {'share': Decimal, 'total': Decimal, 'over': Decimal}."""
    account_dec = Decimal(account)

    share = account_dec / guests
    share = share.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    total = share * guests          # сколько соберём со всех гостей
    over = total - account_dec      # переплата (или недоплата, если < 0)

    print(f"Account: {account_dec}")
    print(f"Guests: {guests}")
    print(f"Share: {share}")
    print(f"Sum: {total} (over {over})")

    return {"share": share, "total": total, "over": over}


# ============================================================
# Тесты (assert)
# ============================================================

if __name__ == "__main__":
    # 3.1
    assert safe_input("42") == "OK: 42"
    assert safe_input("-7") == "OK: -7"
    assert safe_input("abc") == "Not a number"
    assert safe_input("3.14") == "Not a number"

    # 3.2
    assert parse_name_age("Ivan:24") == "Hello, Ivan! Next year you are 25."
    assert parse_name_age("Anna:30") == "Hello, Anna! Next year you are 31."

    # 3.3
    receipt = format_receipt("apple", 15.5, 3)
    assert "apple" in receipt
    assert "15.50" in receipt
    assert "46.50" in receipt

    # 4.1
    assert exact_total("19.99", 3, "13") == "67.77"

    # 4.2
    fs, feq, ds, deq = compare_float_decimal()
    assert feq is False
    assert deq is True

    # 4.3
    assert sum_fractions("1/3", "1/6") == "1/2"
    assert sum_fractions("1/2", "1/2") == "1"

    # 4.4
    res = split_bill("1234.56", 7)
    assert res["share"] == res["share"].quantize(res["share"])
    assert res["total"] >= res["over"]

    print("p4_advanced: все тесты пройдены")
