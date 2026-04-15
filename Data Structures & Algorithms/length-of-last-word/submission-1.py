class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        lenOfWord = 0

        if i == 0:
            return 1

        while i:
            if s[i] != " ":
                lenOfWord += 1
                if s[i - 1] == " ":
                    return lenOfWord
            i -= 1

            
        