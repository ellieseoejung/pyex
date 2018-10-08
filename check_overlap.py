'''
Check two lists to find overlap and output sorted intersection
Input "1,2,3,4,5;6,4,3" 
Expected Output "3,4"
'''

import sys

for line in sys.stdin:
  first,second = line.strip().split(";")
  first_array = first.split(",")
  second_array = second.split(",")
  print("FIRST: {}".format(first))
  print("SECOND: {}".format(second))
  print("FIRST ARRAY: {}".format(first_array))
  print("SECOND ARRAY: {}".format(second_array))
  first_set = set(first_array)
  second_set = set(second_array)
  print("FIRST SET: {}".format(first_set))
  print("SECOND SET: {}".format(second_set))

  sorted_set = sorted(list(first_set.intersection(second_set)))

  print(",".join(sorted_set))
