class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tracker = 1
        
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[tracker] = nums[i]
                tracker += 1
            
        return tracker
            