import heapq


def heap_sort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for _ in range(len(h))]


def min_cost_to_connect_cables_sorted(cable_lengths):
    sorted_cables = heap_sort(cable_lengths)
    total_cost = 0

    while len(sorted_cables) > 1:
        first = sorted_cables.pop(0)
        second = sorted_cables.pop(0)

        cost = first + second
        total_cost += cost

        sorted_cables.append(cost)
        sorted_cables = heap_sort(sorted_cables)

    return total_cost


cable_lengths = [4, 3, 2, 6, 10, 7, 4]
min_cost = min_cost_to_connect_cables_sorted(cable_lengths)
print("Min cost:", min_cost)


def merge_k_lists(lists):
    min_heap = []
    for i, sublist in enumerate(lists):
        if sublist:
            heapq.heappush(min_heap, (sublist[0], i, 0))

    result = []
    while min_heap:
        value, list_idx, element_idx = heapq.heappop(min_heap)
        result.append(value)
        if element_idx + 1 < len(lists[list_idx]):
            next_tuple = (lists[list_idx][element_idx + 1],
                          list_idx, element_idx + 1)
            heapq.heappush(min_heap, next_tuple)

    return result


lists = [[0, 4, 5], [1, 3, 7], [6, 9]]
merged_list = merge_k_lists(lists)
print("Sorted List:", merged_list)
