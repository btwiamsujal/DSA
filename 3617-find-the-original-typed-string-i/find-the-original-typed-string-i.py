class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        count = 1
        for i in range(1, len(word)):
            if word[i] == word[i-1]:
                count += 1
        return count 
