"""
ДЗ презентации 5, повышенный уровень, задача 2.
Время: 25–35 минут.

Тема: минимальное число платформ.

Условие:
    Даны arrivals и departures поездов.
    Верните минимальное число платформ.

Пример:
    arrivals   = [900, 940, 950, 1100, 1500, 1800]
    departures = [910, 1200, 1120, 1130, 1900, 2000]
    Ответ: 3
"""


def min_platforms(arrivals: list, departures: list) -> int:
    # сортируем отдельно прибытия и отправления
    arr = sorted(arrivals)
    dep = sorted(departures)

    i = 0           # следующее прибытие
    j = 0           # следующее отправление
    busy = 0        # сколько платформ занято сейчас
    max_busy = 0    # максимум за всё время — это и есть ответ

    while i < len(arr):
        if arr[i] < dep[j]:
            # поезд приехал раньше, чем кто-то уехал
            busy = busy + 1
            i = i + 1
            if busy > max_busy:
                max_busy = busy
        else:
            # поезд уехал (при равном времени сначала отправление,
            # чтобы освободившуюся платформу мог занять новый поезд)
            busy = busy - 1
            j = j + 1

    return max_busy


if __name__ == "__main__":
    assert min_platforms([], []) == 0
    assert min_platforms([900], [910]) == 1
    assert min_platforms(
        [900, 940, 950, 1100, 1500, 1800],
        [910, 1200, 1120, 1130, 1900, 2000]
    ) == 3
    assert min_platforms([100, 200, 300], [150, 250, 350]) == 1
    print("task_02 (p5 advanced): тесты пройдены")
