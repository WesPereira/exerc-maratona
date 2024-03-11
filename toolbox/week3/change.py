def change(money):
    answer = 0
    res = money % 10
    answer = int(money/10)
    answer += int(res/5)
    res = res % 5
    return answer + res


if __name__ == '__main__':
    m = int(input())
    print(change(m))
