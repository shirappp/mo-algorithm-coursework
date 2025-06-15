import math
from collections import defaultdict

# Класс одного запроса
class Query:
    def __init__(self, l, r, idx):
        self.l = l
        self.r = r
        self.idx = idx

    def __lt__(self, other):
        block_size = Query.block_size
        if self.l // block_size != other.l // block_size:
            return self.l < other.l
        return self.r < other.r if (self.l // block_size) % 2 == 0 else self.r > other.r

def mo_algorithm(arr, queries):
    n = len(arr)
    Query.block_size = int(math.sqrt(n))  # Размер блока

    # Сортировка запросов по Мо
    queries.sort()

    freq = defaultdict(int)  # Словарь частот
    answers = [0] * len(queries)  # Ответы на запросы
    current_answer = 0  # Текущее количество различных элементов

    L, R = 0, -1  # Текущий отрезок [L, R]

    def add(x):
        nonlocal current_answer
        freq[x] += 1
        if freq[x] == 1:
            current_answer += 1

    def remove(x):
        nonlocal current_answer
        freq[x] -= 1
        if freq[x] == 0:
            current_answer -= 1

    # Основной цикл по запросам
    for q in queries:
        while L > q.l:
            L -= 1
            add(arr[L])
        while R < q.r:
            R += 1
            add(arr[R])
        while L < q.l:
            remove(arr[L])
            L += 1
        while R > q.r:
            remove(arr[R])
            R -= 1
        answers[q.idx] = current_answer

    return answers