from random import randint


def partition3(a, l, r):
   x, j, t = a[l], l, r
   i = j

   while i <= t :
      if a[i] < x:
         a[j], a[i] = a[i], a[j]
         j += 1

      elif a[i] > x:
         a[t], a[i] = a[i], a[t]
         t -= 1
         i -= 1 # remain in the same i in this case
      i += 1   
   return j, t


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
