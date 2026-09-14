class Solution:
    def isValid(self, s: str) -> bool:
        
        # We need a stack to store the chars in s (only openers)
        # We need a dict for opening and closing tags
        # Store each opening bracket into stack
        # The tags mus tbe closed in correct order

        # Base case if len is < 1
        if len(s) <= 1:
            return False
        # Init dict {"close": "open"}
        openClose = {")": "(", "}":"{", "]":"["}

        # Stack
        stack = []

        for c in s:
            # We check if opener in dict (valid one)
            if c in openClose:
                # If the open tag is indeed in the stack
                if stack and stack[-1] == openClose[c]:
                    stack.pop()

                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
            
