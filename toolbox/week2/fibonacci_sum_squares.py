def fibonacci_sum_squares(n):
    fibs = [0] * 60

    fibs[0] = 0
    fibs[1] = 1

    for i in range(2, len(fibs)):
        fibs[i] = fibs[i-1] + fibs[i-2]

    return (fibs[n%60] * fibs[(n+1)%60])%10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))
