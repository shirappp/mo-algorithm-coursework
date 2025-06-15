import matplotlib.pyplot as plt
from collections import defaultdict
import math
import time

arr = [1, 2, 1, 3, 4, 2, 1]
queries = [(0, 4), (1, 3), (2, 6)]

block_size = int(math.sqrt(len(arr)))

class Query:
    def __init__(self, l, r, idx):
        self.l = l
        self.r = r
        self.idx = idx

    def __lt__(self, other):
        if self.l // block_size != other.l // block_size:
            return self.l < other.l
        return self.r < other.r if (self.l // block_size) % 2 == 0 else self.r > other.r

def visualize_mo(arr, queries):
    q_objects = [Query(l, r, i) for i, (l, r) in enumerate(queries)]
    q_objects.sort()

    L, R = 0, -1
    freq = defaultdict(int)
    unique_count = 0
    results = [0] * len(queries)

    def add(x):
        nonlocal unique_count
        freq[x] += 1
        if freq[x] == 1:
            unique_count += 1

    def remove(x):
        nonlocal unique_count
        freq[x] -= 1
        if freq[x] == 0:
            unique_count -= 1

    for q in q_objects:
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

        results[q.idx] = unique_count

        # Визуализация
        plt.figure(figsize=(8, 1.5))
        colors = ['lightgray'] * len(arr)
        for i in range(q.l, q.r + 1):
            colors[i] = 'skyblue'
        plt.bar(range(len(arr)), arr, color=colors)
        plt.title(f"Запрос [{q.l}, {q.r}] — уникальных чисел: {unique_count}")
        plt.xticks(range(len(arr)))
        plt.tight_layout()
        plt.show()
        time.sleep(1)

visualize_mo(arr, queries)