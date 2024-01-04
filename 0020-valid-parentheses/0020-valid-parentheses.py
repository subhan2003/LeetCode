class Solution:
    def isValid(self, s: str) -> bool:
        flag = False
        stack = []
        
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                x = stack.pop()
                if (x == '(' and s[i] == ')') or (x == '[' and s[i] == ']') or (x == '{' and s[i] == '}'):
                       flag = True
                else:
                    return False
                
        return False if len(stack) > 0 else flag
                   
                