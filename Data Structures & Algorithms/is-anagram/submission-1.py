class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        solution = [0] * 27

        for i in range(len(s)):
            solution[ord(s[i]) - ord('a')] += 1
            solution[ord(t[i]) - ord('a')] -= 1
        
        for value in solution:
            if value != 0:
                return False
        return True

        