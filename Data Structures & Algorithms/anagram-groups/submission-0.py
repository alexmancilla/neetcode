class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = []
        hashmap = {}

        for word in strs:
            sorted_word = sorted(word)
            key_word = str(sorted_word)

            if key_word not in hashmap:
                hashmap.setdefault(key_word, []).append(word)
            else:
                hashmap[key_word].append(word)

        for values in hashmap.values():
            sol.append(values)

        return sol
        
        