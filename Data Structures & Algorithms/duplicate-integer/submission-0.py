class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i in range(len(nums)):
            # my breaking condition
            if nums[i] in dict:
                return True
            # appending values
            dict[nums[i]] = i
        
        return False
        
        