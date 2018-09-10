unsorted_score = [37, 89, 41, 65, 91, 53, 37, 100, 100]
high_possible_score = 100 # Given

def high_score(unsorted_score, high_possible_score):
    # store counts of element appearance in input list
    # array size will be equal to high_possible_score
    counting_array = [0] * (high_possible_score + 1) # initialize the array with 0-100 spots
    results_array = [0] * (len(unsorted_score))
    j = 0

    for score in unsorted_score:
        print("FOR LOOP - score: ", score)
        if score <= high_possible_score:
            counting_array[score] += 1
            print("CURRENT SCORE: ", score)

    for i in range(len(counting_array)):
        for k in range(counting_array[i]):
            results_array[j] = i
            j += 1

    return results_array

results = list(high_score(unsorted_score, high_possible_score))
print(results[::-1])
