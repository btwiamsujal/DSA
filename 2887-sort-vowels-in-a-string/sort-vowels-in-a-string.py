class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiouAEIOU"
        vowel_list = []
        result_list = list(s)

        for char in s:
            if char in vowels:
                vowel_list.append(char)

        vowel_list.sort()
        
        vowel_index = 0
        for i in range(len(result_list)):
            if result_list[i] in vowels:
                result_list[i] = vowel_list[vowel_index]
                vowel_index += 1
        return "".join(result_list)