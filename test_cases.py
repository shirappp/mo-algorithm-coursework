from mo_algorithm import mo_algorithm, Query
def run_test_case(arr, raw_queries, expected):
    queries = [Query(l, r, idx) for idx, (l, r) in enumerate(raw_queries)]
    result = mo_algorithm(arr, queries)
    assert result == expected, f"❌ Ошибка: ожидалось {expected}, получено {result}"
    print(f"✅ Тест пройден: {result}")

def main():
    print("Запуск тестов алгоритма Мо...\n")

    # Тест 1: стандартный случай
    run_test_case(
        arr=[1, 2, 1, 3, 4, 2, 1],
        raw_queries=[(0, 4), (1, 3), (2, 6)],
        expected=[4, 3, 4]
    )

    # Тест 2: разные элементы
    run_test_case(
        arr=[5, 1, 2, 1, 5, 3],
        raw_queries=[(0, 5), (1, 4)],
        expected=[4, 3]
    )

    # Тест 3: одинаковые элементы
    run_test_case(
        arr=[7, 7, 7, 7, 7],
        raw_queries=[(0, 4), (1, 3)],
        expected=[1, 1]
    )

    # Тест 4: один элемент в массиве
    run_test_case(
        arr=[42],
        raw_queries=[(0, 0)],
        expected=[1]
    )

    # Тест 5: непересекающиеся запросы
    run_test_case(
        arr=[1, 2, 3, 4, 5, 6],
        raw_queries=[(0, 2), (3, 5)],
        expected=[3, 3]
    )

    print("\n🎉 Все тесты пройдены успешно!")

if __name__ == "__main__":
    main()