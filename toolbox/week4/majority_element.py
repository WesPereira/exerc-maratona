def merge(array1, array2):
    merged_array = []
    i = 0
    j = 0
    while i < len(array1) or j < len(array2):
        if i >= len(array1):
            merged_array.append(array2[j])
            j += 1
            continue
        if j >= len(array2):
            merged_array.append(array1[i])
            i += 1
            continue
        if array1[i] < array2[j]:
            merged_array.append(array1[i])
            i += 1
        else:
            merged_array.append(array2[j])
            j += 1
    return merged_array


def mergesort(elements):
    if len(elements) == 1:
        return elements
    middle = len(elements) // 2
    first_part = mergesort(elements[:middle])
    second_part = mergesort(elements[middle:])
    merged = merge(first_part, second_part)
    return merged


def majority_element_naive(elements):
    sorted_array = mergesort(elements)
    count = 0
    previous_element = -1
    for element in sorted_array:
        if element == previous_element:
            count += 1
            if count > len(sorted_array)/2:
                return 1
        else:
            count = 1
            previous_element = element
    return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_naive(input_elements))
