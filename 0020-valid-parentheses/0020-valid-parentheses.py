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
                x = stack[-1]
                if (x == '(' and s[i] == ')') or (x == '[' and s[i] == ']') or (x == '{' and s[i] == '}'):
                    flag = True
                    stack.pop()
                else:
                    return False
                
        return False if len(stack) > 0 else flag
                   
                