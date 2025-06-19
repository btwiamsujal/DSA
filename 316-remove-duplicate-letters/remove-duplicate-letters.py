class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = {}
        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1

        stack = []
        seen = set()

        for char in s:
            freq[char] -= 1

            if char in seen:
                continue
            while stack and char < stack[-1] and freq[stack[-1]] > 0:
                removed = stack.pop()
                seen.remove(removed)

            stack.append(char)
            seen.add(char)
        
        return ''.join(stack)