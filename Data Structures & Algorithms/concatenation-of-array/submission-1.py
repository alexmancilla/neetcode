class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size = len(nums)
        n = 2
        solution = [None] * (size * n)
        
        for i in range(size):
            solution[i] = nums[i]
            solution[i + size] = nums[i]
        
        return solution