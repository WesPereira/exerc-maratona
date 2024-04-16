def binary_search(keys, query):
    left = 0
    right = len(keys) - 1
    min_key = -1
    while right >= left:
        middle = (left + right)//2
        if keys[middle] == query:
            min_key = middle
            right = middle - 1
        elif keys[middle] > query:
            right = middle - 1
        else:
            left = middle + 1
    return min_key


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
