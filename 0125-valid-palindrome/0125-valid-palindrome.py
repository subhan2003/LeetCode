class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        L = 0
        R = len(newString) - 1
        while L < R:
            if newString[L] != newString[R]:
                return False
            L += 1
            R -= 1
        return True
        
       
        
            