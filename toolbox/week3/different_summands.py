def optimal_summands(n):
    summands = []
    last = 0
    rest = n
    count = 1
    while rest > last:
        summands.append(count)
        last = count
        rest -= count
        count += 1
    summands[-1] += rest
    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
