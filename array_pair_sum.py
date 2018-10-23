'''
Given an integer array, output all pairs that sum up to a specific value k.
'''

def array_pair_sum(input_array, k):
    # k is the target number
    if len(input_array) < 2:
        return
    input_array.sort()
    left, right = (0, len(input_array)-1)

    while left < right:
        sum = input_array[left] + input_array[right]
        if sum == k:
            print("The pair: {}, {}".format(input_array[left], input_array[right]))
            left += 1
        elif sum < k:
            left+= 1
        else:
            right -= 1


input_array = [1, 2, 5, 4, 3]
k = 5
array_pair_sum(input_array, k)
