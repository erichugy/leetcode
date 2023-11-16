from Typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            m = (l + r) //2
            v = nums[m]
            if target == nums[m]: return m
            elif target < nums[m]: r = m
            else:l = m + 1

        return l
