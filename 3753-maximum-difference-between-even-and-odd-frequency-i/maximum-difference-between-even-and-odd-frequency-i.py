class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = Counter(s)
        
        odd_freqs = []
        even_freqs = []

        for ch, count in freq.items():
            if count % 2 == 1:
                odd_freqs.append(count)
            else:
                even_freqs.append(count)

        if not odd_freqs or not even_freqs:
            return 0

        max_diff = float('-inf')
        for odd in odd_freqs:
            for even in even_freqs:
                max_diff = max(max_diff, odd - even)

        return max_diff