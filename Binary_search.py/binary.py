
from tkinter.messagebox import NO


def naive_search(l, target):
    for item in l:
        if item == target:
            return l.index(item)
    return None


numbers = [1, 2, 3, 4, 5, 7, 90, 23, 67]


def binary_search(list, target):
    while True:
        print("--------------")
        mid_point = len(list) // 2
        print("Mid:", mid_point)
        if list[mid_point] == target:
            print("The mid point and the target are the same")
            print(target)
            return list.index(target)
        elif list[mid_point] < target:
            list = list[mid_point:]
            print("The right half of the list is ", list)
        else:
            list = list[:mid_point]
            print("The left half of the list is ", list)


print(binary_search(numbers, 4))


def new_bianry_search(l, target, low=None, high=None):
    if low == None:
        low = 0
    if high == None:
        high = len(l) - 1

    if high < low:
        return -1

    mid_point = (low + high) // 2

    if l[mid_point] == target:
        return mid_point

    elif target < l[mid_point]:
        return new_bianry_search(l, target, low, mid_point - 1)
    else:
        return new_bianry_search(l, target, mid_point + 1, high)


print(new_bianry_search(numbers, 8))
