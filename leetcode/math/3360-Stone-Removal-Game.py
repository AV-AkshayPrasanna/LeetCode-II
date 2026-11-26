class Solution:
    def canAliceWin(self, n):
        k = 10
        w = False
        while n >= k:
            n -= k
            k -= 1
            w = not w
        return w