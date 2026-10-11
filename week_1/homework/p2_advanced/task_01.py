"""
ДЗ презентации 2, повышенный уровень, задача 1.
Время: 20–30 минут.

Тема: арифметические операторы, // и %.

Условие:
    Дано целое число секунд. Переведите его в формат ЧЧ:ММ:СС.
    Используйте только // и %.

Пример:
    In: 3661
    Out: 01:01:01
"""


def seconds_to_hms(seconds: int) -> str:
    # в одном часе 3600 секунд, в одной минуте — 60
    hours = seconds // 3600
    rest = seconds % 3600        # секунды, которые не вошли в целые часы
    minutes = rest // 60
    secs = rest % 60

    # :02d — всегда две цифры, с ведущим нулём (5 -> 05)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


if __name__ == "__main__":
    assert seconds_to_hms(3661) == "01:01:01"
    assert seconds_to_hms(0) == "00:00:00"
    assert seconds_to_hms(59) == "00:00:59"
    assert seconds_to_hms(3600) == "01:00:00"
    print("task_01 (p2 advanced): тесты пройдены")
