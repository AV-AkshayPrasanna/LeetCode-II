class Solution:
    def maximumSaleItems(self, items, budget):
        n = len(items)
        pm = min(p for _, p in items)
        d = [0] * (budget + 1)
        for i in range(n):
            f, p = items[i]
            g = 1 + sum(1 for j in range(n) if j != i and items[j][0] % f == 0)
            for b in range(budget, p - 1, -1):
                if d[b - p] + g > d[b]:
                    d[b] = d[b - p] + g
        return max(d[b] + (budget - b) // pm for b in range(budget + 1))