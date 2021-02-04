def basic_sort(list):
    for element in list:
        element_index = list.index(element)
        previous_element = list[element_index - 1]
        print(element_index, previous_element)
        if element < previous_element:
            element, previous_element = previous_element, element
        # print(index)
        # print(element)
    return list

new_list = ["b", "a", "c"]

print(basic_sort(new_list))
