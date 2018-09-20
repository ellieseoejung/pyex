def binary_search(elem_list, target):
    low = 0
    high = len(elem_list) - 1
    count = 0

    while low <= high:
        mid = (high + low) // 2

        if elem_list[mid] == target:
            count += 1
            return True, count
        elif target < elem_list[mid]:
            count += 1
            high = mid - 1
        else:
            count += 1
            low = mid + 1

    return False, count

elem_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
results = binary_search(elem_list, target)
print("Results: {} counts".format(results))
