class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l2 = [i for i in range(max(nums) + 1)]

        if len(l2) == len(nums):
            return max(nums) + 1
        else:
            return (list(set(l2) - set(nums))[0])
