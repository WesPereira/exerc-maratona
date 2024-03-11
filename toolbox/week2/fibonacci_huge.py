def pisano_period(m):
    previous = 0
    current  = 1

    for i in range(m*m):
        previous, current = current, (previous + current) % m
        if (previous == 0 and current == 1):
            return i + 1


def fibonacci_huge_naive(n, m):

    pis = pisano_period(m)
    n = n % pis
    previous = 0
    current  = 1

    if n <= 1:
        return n

    for _ in range(n-1):
        previous, current = current, previous + current

    return current % m


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))
