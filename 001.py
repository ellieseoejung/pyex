class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict()

        # for i in range(len(nums)):
        #     j = nums[i]
        #
        #     if (target - j) in d:
        #         return d[target - j], i
        #
        #     d[j] = i

        for i, value in enumerate(nums):
            if (target - value) in d:
                return d[target - value], i

            d[value] = i
