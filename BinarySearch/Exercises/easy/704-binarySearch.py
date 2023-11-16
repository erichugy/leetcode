from Typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)

        while i < j:
            m = (i + j)//2
            v = nums[m]
            if v == target: return m
            elif v > target:
                j = m
            else:
                i= m+1

        return -1
