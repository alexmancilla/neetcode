class Solution:
    def isValid(self, s: str) -> bool:
        openChars = "[[("
        closedChars = ")]}"
        stack = []
        hashtable = {"{":"}", "[":"]", "(":")"}

        if len(s) == 1:
            return False

        for i in range(len(s)):
            if s[i] in closedChars:
                if len(stack) == 0:
                    return False
                if stack.pop() != s[i]:
                    return False
            else:
                stack.append(hashtable[s[i]])

        return stack == []