class Solution:
    def scoreOfString(self, s: str) -> int:
        l, r = 0, 1
        score = 0

        while r < len(s):
            l_value = ord(s[l])
            r_value = ord(s[r])
            score = score + abs(l_value - r_value)
            l += 1
            r += 1
        
        return score
        