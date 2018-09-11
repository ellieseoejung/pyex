int_list = [1, 7, 0, 3, 4] # [1, 2, 3, 4, 5]

def except_index(int_list):
    left_list = [1] * len(int_list)
    right_list = [1] * len(int_list)
    new_list = [1] * len(int_list)

    left_list[0] = int_list[0]
    right_list[len(int_list)-1] = int_list[len(int_list)-1]

    start = 1

    for i in range(start, len(int_list)-1):
        left_list[i] = int_list[i] * left_list[i - 1]
        print("NEW left LIST: {}".format(left_list))
        right_list[-i-1] = int_list[-i-1] * right_list[-i]
        print("NEW right LIST: {}".format(right_list))

    new_list[0] = right_list[1]
    new_list[len(int_list)-1] = left_list[-2] # a[-x] == a[len(a)-x]
    for i in range(1, len(int_list)-1):
        print("curr i : {}".format(i))
        new_list[i] = left_list[i-1] * right_list[i+1]
        print("curr new_list[i]: {} = left_list: {} * right_list: {}".format(new_list[i], left_list[i-1], right_list[i+1]))

    return new_list

results = except_index(int_list)
print("RESULTS: {}".format(results))
