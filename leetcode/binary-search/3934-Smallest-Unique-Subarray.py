import random
from collections import Counter

class Solution:
    def smallestUniqueSubarray(self, nums):
        n = len(nums)
        M = (1 << 61) - 1
        B = random.randrange(10**6, M - 1)
        H = [0] * (n + 1)
        P = [1] * (n + 1)
        for i, x in enumerate(nums):
            H[i + 1] = (H[i] * B + x) % M
            P[i + 1] = P[i] * B % M
        def f(L):
            c = Counter((H[i + L] - H[i] * P[L]) % M for i in range(n - L + 1))
            return 1 in c.values()
        l, r = 1, n
        while l < r:
            m = (l + r) // 2
            if f(m):
                r = m
            else:
                l = m + 1
        return l