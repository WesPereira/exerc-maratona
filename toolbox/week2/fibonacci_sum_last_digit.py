def fibonacci_sum(n):
    fibs = [0] * 60

    fibs[0] = 0
    fibs[1] = 1

    m = n % 60
    n_times = int(n / 60)

    sum_fib = 1
    for i in range(2, len(fibs)):
        fibs[i] = fibs[i-1] + fibs[i-2]
        sum_fib += fibs[i] % 10

    tot = n_times * sum_fib

    for i in range(m+1):
        tot += fibs[i] % 10

    return tot % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))
