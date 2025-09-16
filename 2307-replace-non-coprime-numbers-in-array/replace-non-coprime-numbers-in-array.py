from fractions import gcd

class Solution:
    def replaceNonCoprimes(self, nums):
        stack = []
        for num in nums:
            stack.append(num)
            while len(stack) > 1:
                a = stack[-1]
                b = stack[-2]
                g = gcd(a, b)
                if g == 1:
                    break
                l = a * b // g
                stack.pop()
                stack.pop()
                stack.append(l)
        return stack
