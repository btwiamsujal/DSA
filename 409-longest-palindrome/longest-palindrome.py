class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        my_dict = {}
        for ch in s:
            if ch in my_dict:
                my_dict[ch] += 1
            else:
                my_dict[ch] = 1

        ans = 0
        odd_found = False
        # print(my_dict)
        for ch in my_dict:
            if my_dict[ch] % 2 == 0:
                ans += my_dict[ch]
            else:
                ans += my_dict[ch] - 1
                odd_found = True
        
        if odd_found == True:
            return ans+1
        return ans

            

        