def binary_search(l, element):
    left = 0
    right = len(l) - 1
    while left < right:
        print((left,right))
        middle = (right + left) // 2
        if l[middle] == element:
            return middle
        elif l[middle] > element:
            right = middle - 1
        elif l[middle] < element:
            left = middle + 1
    return left
