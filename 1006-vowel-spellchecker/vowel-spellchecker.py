class Solution(object):
    def spellchecker(self, wordlist, queries):
        word_set = set(wordlist)
        lower_map = {}
        vowel_map = {}

        def devowel(word):
            return "".join('*' if c in 'aeiou' else c for c in word)

        for word in wordlist:
            low = word.lower()
            if low not in lower_map:
                lower_map[low] = word
            dev = devowel(low)
            if dev not in vowel_map:
                vowel_map[dev] = word

        ans = []
        for q in queries:
            if q in word_set:
                ans.append(q)
                continue
            low = q.lower()
            if low in lower_map:
                ans.append(lower_map[low])
                continue
            dev = devowel(low)
            if dev in vowel_map:
                ans.append(vowel_map[dev])
                continue
            ans.append("")
        return ans
