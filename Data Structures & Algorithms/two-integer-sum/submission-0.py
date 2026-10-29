class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict= {}
        
        for i in range(len(nums)):
            tobefind = target - nums[i]
            if tobefind in dict:
                return [dict[tobefind],i]
            dict[nums[i]] = i
        
        return []