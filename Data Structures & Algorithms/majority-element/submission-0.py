class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major_nums = []
        major = None

        for num in nums:
            if num not in major_nums and major is None:
                major_nums.append(num)
                major = num
            elif num in major_nums:
                major_nums.append(num)
            elif num not in major_nums and major != None:
                if major_nums  == []:
                    major_nums.append(num)
                    major = num
                else:
                    major_nums.pop()

        
        if major_nums[0] == major:
            return major

        return false

        