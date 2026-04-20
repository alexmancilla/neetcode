class Solution:

    def encode(self, strs: List[str]) -> str:
        def generateWordLen(wl):
            if wl > 99:
                return str(wl)
            if wl > 9:
                value = "0" + str(wl)
                return value
            if wl <= 9:
                value = "00" + str(wl)
                return value

        s = ""
        for word in strs:
            word_len = len(word)
            wl = generateWordLen(word_len)
            encode_word = "len" + wl + word
            s += encode_word
        return s
            
    def decode(self, s: str) -> List[str]:
        sol = []
        i = 0
        
        while i < len(s):
            if s[i] == "l" and s[i + 1] == "e" and s[i + 2] == "n":
                word = ""
                word_len = s[i + 3] + s[i + 4] + s[i + 5]
                wl = int(word_len)

                tempWord = ""
                start = i + 6
                for j in range(wl):
                    tempWord += s[start + j]
                        
                sol.append(tempWord)
                i = i + 6 + (wl)
        return sol
                


