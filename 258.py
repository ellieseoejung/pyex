class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        text_num = str(num)
        one_letter = list(text_num)

        while True:
            output = 0
            for letter in range(0, len(one_letter)):
                output += int(one_letter[letter])
            one_letter = list(str(output))
            if output < 10:
                return output
