def basic_sort(list):

    if len(list) <= 1:
        return list
    else:
        pivot = list.pop()

    larger_items = []
    smaller_items = []

    for i in list:
        if i > pivot:
            larger_items.append(i)
        else:
            smaller_items.append(i)

    return basic_sort(smaller_items) + [pivot] + basic_sort(larger_items)

new_list = [1, 0, 6, 7, 8, 4, 5, 2, 8, 5, 6, 4, 6, 7, 8, 4]

print(basic_sort(new_list))
