class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
     
        for nums in nums:
            if nums in hashset:
                return True
            else:
                hashset.add(nums) 
           
        return False 