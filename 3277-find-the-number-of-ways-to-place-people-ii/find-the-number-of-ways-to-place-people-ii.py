class Solution:
    def numberOfPairs(self, points):
        n = len(points)
        if n < 2:
            return 0

        xs = [p[0] for p in points]
        ys = [p[1] for p in points]
        minc = min(min(xs), min(ys))
        maxc = max(max(xs), max(ys))
        b = (maxc - minc + 1).bit_length()
        sh = b
        m = (1 << sh) - 1

        # pack points: x asc, y desc
        data = []
        for x, y in points:
            x -= minc
            y = m - (y - minc)
            data.append((x << sh) + y)

        # sort by (x asc, y desc) automatically
        data.sort()

        t = 0
        for i in range(n - 1, 0, -1):
            y = m - (data[i] & m)
            ym = m
            for j in range(i - 1, -1, -1):
                z = m - (data[j] & m)
                good = (z >= y) and (ym > z)
                if good:
                    t += 1
                    ym = z
                if y == z:
                    break
        return t
