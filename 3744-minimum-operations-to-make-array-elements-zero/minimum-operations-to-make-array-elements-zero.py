import math

class Solution(object):
    def calc(self, l, r):
        op = r - l + 1
        sti = int(math.log(l) / math.log(4))  # start power of 4
        eni = int(math.log(r) / math.log(4))  # end power of 4
        p = 4 ** (sti + 1)  # first range ending point

        while sti <= eni:
            nr = min(r, p)  # ending of current range
            el = nr - l  # number of elements

            if nr == r and sti == eni:
                el += 1
            op += el * sti  # adding range operations
            sti += 1
            l = p  # next range start
            p *= 4  # next range end

        return (op + 1) // 2  # pairing in 2s

    def minOperations(self, queries):
        ans = 0
        for l, r in queries:
            ans += self.calc(l, r)
        return ans
