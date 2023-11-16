class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        #The perfect square lies between 1 and num/2 inclusively

        l = 1
        r = num//2 + 1
        m = 1
        while l < r:
            m = (l + r)//2
            v = m**2
            if v == num:
                return True
            elif v > num:
                r = m
            else:
                l = m +1

        return m ** 2 == num
