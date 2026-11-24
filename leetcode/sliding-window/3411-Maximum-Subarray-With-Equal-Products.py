from math import gcd

class Solution:
    def maxLength(self, nums):
        r = 0
        for i in range(len(nums)):
            p, g, l = 1, 0, 1
            for j in range(i, len(nums)):
                x = nums[j]
                p *= x
                g = gcd(g, x)
                l = l * x // gcd(l, x)
                if p == g * l:
                    r = max(r, j - i + 1)
        return r