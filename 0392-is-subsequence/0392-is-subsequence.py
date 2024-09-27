class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = 0

        i = 0
        j = 0
        while i < len(t) and j < len(s):
            if s[j] == t[i]:
                i += 1
                j += 1
                count += 1
            elif s[j] != t[i]:
                i += 1
                
            
        if count == len(s):
            return True
        else:
            return False

            
