class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        counter = 0 
        L = 0
        curr_sum = 0
        
        for R in range(len(arr)):
            curr_sum = curr_sum + arr[R]
            if R - L + 1 == k:
                if curr_sum/k >= threshold:
                    counter = counter + 1
                curr_sum = curr_sum - arr[L]
                L = L + 1
               
        return counter
            
        

 



