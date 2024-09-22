class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        storage = {}
        for i in nums:
            if i in storage:
                storage[i] += 1
            else:
                storage[i] = 1
            
        return max(storage, key=storage.get)
        