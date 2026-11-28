class Solution:
    def maximumSaleItems(self, items, budget):
        n = len(items)
        c = [0] * (n + 1)
        for f, _ in items:
            c[f] += 1
        m = [0] * (n + 1)
        for d in range(1, n + 1):
            m[d] = sum(c[d::d])
        pm = min(p for _, p in items)
        k = 0
        for f, p in sorted(items, key=lambda x: x[1]):
            if p >= 2 * pm:
                break
            g = m[f] - 1
            if not g:
                continue
            t = min(g, budget // p)
            budget -= t * p
            k += t
            if t < g:
                break
        return 2 * k + budget // pm