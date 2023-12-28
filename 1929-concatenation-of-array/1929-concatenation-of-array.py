class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = 2 * len(nums)
        array = [None] * length
        
        for i in range(len(nums)):
            array[i] = nums[i]
            array[i + len(nums)] = nums[i]
        
        return array
