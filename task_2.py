from typing import List, Dict
from dataclasses import dataclass

@dataclass
class PrintJob:
    id: str
    volume: float
    priority: int
    print_time: int

@dataclass
class PrinterConstraints:
    max_volume: float
    max_items: int


def optimize_printing(print_jobs: List[Dict], constraints: Dict) -> Dict:
    """
    Оптимізує чергу 3D-друку згідно з пріоритетами та обмеженнями принтера.
    Використовує жадібний підхід.
    """
    # Перетворення у dataclass
    jobs = [PrintJob(**job) for job in print_jobs]
    printer = PrinterConstraints(**constraints)

    # Сортуємо за пріоритетом (1 — найвищий), потім за часом
    jobs.sort(key=lambda j: (j.priority, j.print_time))

    total_time = 0
    print_order = []
    group = []
    current_volume = 0

    for job in jobs:
        # Якщо додавання моделі перевищує обмеження — друкуємо групу
        if (len(group) >= printer.max_items) or (current_volume + job.volume > printer.max_volume):
            # Час друку групи = макс. час однієї моделі
            group_time = max(j.print_time for j in group)
            total_time += group_time
            print_order.extend(j.id for j in group)

            # Очищаємо групу
            group = []
            current_volume = 0

        # Додаємо поточну модель у групу
        group.append(job)
        current_volume += job.volume

    # Друкуємо останню групу
    if group:
        group_time = max(j.print_time for j in group)
        total_time += group_time
        print_order.extend(j.id for j in group)

    return {
        "print_order": print_order,
        "total_time": total_time
    }


# 🔹 Тестування
def test_printing_optimization():
    test1_jobs = [
        {"id": "M1", "volume": 100, "priority": 1, "print_time": 120},
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
        {"id": "M3", "volume": 120, "priority": 1, "print_time": 150}
    ]

    test2_jobs = [
        {"id": "M1", "volume": 100, "priority": 2, "print_time": 120},
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
        {"id": "M3", "volume": 120, "priority": 3, "print_time": 150}
    ]

    test3_jobs = [
        {"id": "M1", "volume": 250, "priority": 1, "print_time": 180},
        {"id": "M2", "volume": 200, "priority": 1, "print_time": 150},
        {"id": "M3", "volume": 180, "priority": 2, "print_time": 120}
    ]

    constraints = {
        "max_volume": 300,
        "max_items": 2
    }

    print("Тест 1 (однаковий пріоритет):")
    r1 = optimize_printing(test1_jobs, constraints)
    print(f"Порядок друку: {r1['print_order']}")
    print(f"Загальний час: {r1['total_time']} хвилин")

    print("\nТест 2 (різні пріоритети):")
    r2 = optimize_printing(test2_jobs, constraints)
    print(f"Порядок друку: {r2['print_order']}")
    print(f"Загальний час: {r2['total_time']} хвилин")

    print("\nТест 3 (перевищення обмежень):")
    r3 = optimize_printing(test3_jobs, constraints)
    print(f"Порядок друку: {r3['print_order']}")
    print(f"Загальний час: {r3['total_time']} хвилин")


if __name__ == "__main__":
    test_printing_optimization()
