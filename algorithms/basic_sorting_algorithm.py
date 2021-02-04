def basic_sort(list):
    iterator = 0
    # iterator2 = 0
    for i in range(len(list)):
        if iterator > 0:
            print(list[iterator], list[iterator - 1])
            if list[iterator] < list[iterator - 1]:
                list[iterator], list[iterator - 1] = list[iterator - 1], list[iterator - 1]
            iterator += 1
    # for element in list:
    #     element_index = list.index(element)
    #     previous_element = list[element_index - 1]
    #     print(element_index, previous_element)
    #     if element < previous_element:
    #         element, previous_element = previous_element, element
        # print(index)
        # print(element)
    return list

new_list = ["b", "a", "c"]

print(basic_sort(new_list))
