"""
Презентация 3 — повышенный уровень.
Задачи про алгоритмы: проверка дубликатов, оценка сложности,
улучшение решения с O(n^2) до O(n).
"""

import time

# ============================================================
# Задача 1. Проверка дубликатов (решение коллеги)
# ============================================================
# Условие:
#   Дан список целых чисел nums. Необходимо определить,
#   содержит ли список повторяющиеся элементы.
#   Вернуть True, если хотя бы одно значение встречается
#   больше одного раза, иначе False.
#
# Ограничения:
#   0 <= n <= 100_000
#   -10^9 <= nums[i] <= 10^9
#
# Требуется:
#   1) проверить корректность решения коллеги;
#   2) определить сложность в лучшем и худшем случаях;
#   3) построить входные данные большого размера;
#   4) найти узкое место;
#   5) реализовать улучшенное решение;
#   6) сравнить оба решения.
#
# Ответы:
#   1) Решение коллеги верное: оно сравнивает каждую пару
#      элементов ровно один раз.
#   2) Лучший случай O(1): повтор в самом начале, например [5, 5].
#      Худший случай O(n^2): повторов нет, проверяются все пары.
#   3) Большие данные: list(range(100_000)) — повторов нет,
#      это худший случай.
#   4) Узкое место — вложенный цикл: для каждого элемента
#      заново просматривается весь остаток списка.
#   5) Улучшение: хранить встреченные числа в set,
#      проверка "x in set" в среднем работает за O(1).
#   6) Сравнение — в функции compare_solutions() ниже.


def has_duplicates_slow(nums: list) -> bool:
    """Решение коллеги за O(n^2)."""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


def has_duplicates_fast(nums: list) -> bool:
    """
    Улучшенное решение.
    Сложность: O(n) по времени, O(n) по памяти.
    """
    seen = set()  # числа, которые уже встречались

    for num in nums:
        if num in seen:
            return True  # нашли повтор
        seen.add(num)

    return False


def compare_solutions():
    """Сравнить время работы двух решений на одном списке."""
    # 5000 элементов: на 100_000 медленное решение работало бы очень долго
    data = list(range(5000))

    start = time.time()
    has_duplicates_slow(data)
    slow_time = time.time() - start

    start = time.time()
    has_duplicates_fast(data)
    fast_time = time.time() - start

    print(f"Медленное решение: {slow_time:.4f} сек")
    print(f"Быстрое решение:   {fast_time:.4f} сек")


# ============================================================
# Задача 2. Оценка сложности фрагментов
# ============================================================
# Условие:
#   Определите временную сложность каждого фрагмента.
#   Ответ запишите в виде строки: "O(1)", "O(log n)", "O(n)",
#   "O(n log n)", "O(n^2)".
#
# Фрагмент A:
#   for x in items:
#       print(x)
#
# Фрагмент B:
#   for x in items:
#       for y in items:
#           print(x, y)
#
# Фрагмент C:
#   i = 0
#   while i < n:
#       i *= 2
#
# Фрагмент D:
#   for x in items:
#       pass
#   for x in items:
#       for y in items:
#           pass


def complexity_a() -> str:
    # один проход по списку
    return "O(n)"


def complexity_b() -> str:
    # вложенный цикл: n * n
    return "O(n^2)"


def complexity_c() -> str:
    # i удваивается, до n доходит за ~log2(n) шагов.
    # (при i = 0, как в условии, цикл был бы бесконечным —
    # подразумевается i = 1)
    return "O(log n)"


def complexity_d() -> str:
    # n + n^2, главное слагаемое — n^2
    return "O(n^2)"


# ============================================================
# Тесты
# ============================================================

if __name__ == "__main__":
    assert has_duplicates_slow([]) is False
    assert has_duplicates_slow([1]) is False
    assert has_duplicates_slow([1, 2, 3]) is False
    assert has_duplicates_slow([1, 2, 1]) is True
    assert has_duplicates_slow([5, 5]) is True

    assert has_duplicates_fast([]) is False
    assert has_duplicates_fast([1, 2, 3]) is False
    assert has_duplicates_fast([1, 2, 1]) is True

    data = list(range(100_000))
    assert has_duplicates_fast(data) is False
    data2 = list(range(99_999)) + [0]
    assert has_duplicates_fast(data2) is True

    assert complexity_a() == "O(n)"
    assert complexity_b() == "O(n^2)"
    assert complexity_c() == "O(log n)"
    assert complexity_d() == "O(n^2)"

    compare_solutions()

    print("p3_advanced: все тесты пройдены")
