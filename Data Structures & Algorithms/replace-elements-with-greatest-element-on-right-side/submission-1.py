class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxNum = -1
        n = len(arr)
        ans = [0] * n

        for i in range(n - 1, -1, -1):
            ans[i] = maxNum
            maxNum = max(arr[i], maxNum)
        return ans

        