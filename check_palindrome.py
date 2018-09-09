from collections import defaultdict

input_string = "cicici" # More test cases: "civic", "civil", "aabba"

def check_palindrome(input_string):
    input_dictionary = defaultdict(int)
    odd_count = 0

    for i in input_string:
        input_dictionary[i] += 1
        if input_dictionary[i] % 2 == 0:
            odd_count -= 1
        else:
            odd_count += 1

    if len(input_string) % 2 == 0:
        # The length of the input string is even, there should be letters with only even count.
        return odd_count == 0
    else:
        # The length of the input string is odd, there should be only one letter that have odd count.
        return odd_count == 1

results = check_palindrome(input_string)
print(results)
