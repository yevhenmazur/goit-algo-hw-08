import heapq

def merge_k_lists_alt(l: list) -> list:
    '''O(n log(k))'''

    heap = []

    # Додаю перший елемент кожного списку до купи
    for i, sorted_list in enumerate(l):
        if sorted_list:
            # Використовую кортедж для того щоб додати до купи елемет,
            # а також інформацію про те з якого він списка і його індекс
            heapq.heappush(heap, (sorted_list[0], i, 0))

    result = []

    # Поки купа не порожня, витягую найменший елемент і додаю його до результату
    while heap:
        value, list_idx, element_idx = heapq.heappop(heap)
        result.append(value)

        # Якщо в цьому списку ще є елементи, додаємо до купи наступний
        if element_idx + 1 < len(l[list_idx]):
            next_tuple = (l[list_idx][element_idx + 1],
                          list_idx, element_idx + 1)
            heapq.heappush(heap, next_tuple)

    return result

# Оце я сам придумав, а merge_k_lists_alt() то чат підказав
def merge_k_lists(l):
    '''O(n log(n))'''

    heap = []

    # Додаєю всі елементи в одну купу
    for sorted_list in l:
        for element in sorted_list:
            heapq.heappush(heap, element)

    result = []

    # Витягую елементи з купи і формую відсортований список
    while heap:
        result.append(heapq.heappop(heap))

    return result


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
# merged_list = merge_k_lists(lists)
merged_list = merge_k_lists_alt(lists)

print("Відсортований список:", merged_list)
