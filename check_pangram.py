'''
check pangram and return the missing alphabet letters in order
Input "The quick brown fox jumps over the lazy dog"
Expected Ouput NULL

Input2 "The quick bro fo jumps over the lazy dog"
Expected Output nwx
'''

import sys, string

for line in sys.stdin:
    line_set = set(line.lower().strip())
    alphabet_set = set(string.ascii_lowercase)
    # print(alphabet_set.difference(line_set))

    if alphabet_set.difference(line_set):
        print("".join(sorted(list(alphabet_set.difference(line_set)))))
    else:
        print("NULL")
