class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if nums == []:
            return None

        nums = sorted(nums)
        

        for i in range(len(nums)):
            if i != nums[i]:
                return i
        
        return i+1