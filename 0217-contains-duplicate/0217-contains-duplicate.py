class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        countMap = set()
     
        for nums in nums:
            if nums in countMap:
                return True
            else:
                countMap.add(nums) 
           
        return False     