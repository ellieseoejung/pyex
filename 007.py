class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x < 0:
            num_string = str(-x)
            reversed_num = int("".join(reversed(num_string)))
            reversed_num = -(reversed_num)
        else:
            num_string = str(x)
            reversed_num = int("".join(reversed(num_string)))
        if reversed_num < (-2 ** 31) or reversed_num > (2**31)-1:
            return 0
        else:
            return reversed_num
