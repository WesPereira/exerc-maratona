def fibonacci_partial_sum(m, n):
    fibs = [0] * 60

    fibs[0] = 0
    fibs[1] = 1

    rest_m = m % 60
    rest_n = n % 60
    n_times = int((n - m) / 60)

    sum_fib = 1
    for i in range(2, len(fibs)):
        fibs[i] = fibs[i-1] + fibs[i-2]
        sum_fib += fibs[i] % 10

    if n_times < 1:
        sum_fib = 0
        for i in range(rest_m, rest_n+1):
            sum_fib += fibs[i] % 10
        return sum_fib % 10

    tot = n_times * sum_fib

    for i in range(rest_m, 60):
        tot += fibs[i] % 10

    for i in range(rest_n+1):
        tot += fibs[i] % 10

    return tot % 10


if __name__ == '__main__':
    m, n = map(int, input().split())
    print(fibonacci_partial_sum(m,n))
