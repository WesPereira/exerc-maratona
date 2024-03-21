def max_dot_product(first_sequence, second_sequence):
    first_sorted = sorted(first_sequence, reverse=True)
    second_sorted = sorted(second_sequence, reverse=True)

    return sum([f*s for s, f in list(zip(first_sorted, second_sorted))])


if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))
    
