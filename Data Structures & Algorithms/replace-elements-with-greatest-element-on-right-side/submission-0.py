class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        ans = []

        for i in range(len(arr)):
            maxNum = 0
            for j in range(i + 1, len(arr)):
                maxNum = max(arr[j], maxNum)
            
            if i == len(arr) - 1:
                ans.append(-1)
                return ans
            
            ans.append(maxNum)
        return ans
        