from itertools import permutations


def to_same_size(num_str, size):
    while len(num_str) < size:
        num_str += num_str[0]
    return num_str

def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    max_size = -1
    for num in numbers:
        if len(num) > max_size:
            max_size = len(num)

    new_nums = [(to_same_size(num, max_size), num) for num in numbers]

    sorted_nums = sorted(new_nums, key=lambda x: (int(x[0]), 1- len(x[1])), reverse=True)

    largest = ""

    for _, num in sorted_nums:
        largest += num

    return largest


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_naive(input_numbers))
