import heapq

cabels_heap = [3, 5, 6, 1]
cost = 0

heapq.heapify(cabels_heap)

while len(cabels_heap) > 1:
    cabel_1 = heapq.heappop(cabels_heap)
    cabel_2 = heapq.heappop(cabels_heap)
    joined_cabel = cabel_1 + cabel_2
    cost += joined_cabel
    heapq.heappush(cabels_heap, joined_cabel)

print(f"Кабелі з'єднано з витратами {cost}")
