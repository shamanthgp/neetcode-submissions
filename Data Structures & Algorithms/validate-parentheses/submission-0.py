class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        Closetoopen = { ")": "(","}":"{", "]":"[" }

        for c in s:
            if c in Closetoopen:
                if stack and stack[-1] == Closetoopen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        if not stack:
            return True
        else:
            return False
        
