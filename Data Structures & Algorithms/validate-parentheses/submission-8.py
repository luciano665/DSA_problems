class Solution:
    def isValid(self, s: str) -> bool:

        # We will use a stack to store all opening brackets
        # if is a closing one the opening pair should be at the top of the stack
        # A way to check if we have the valid pair using. dict 
        # If we dont find the oprening we return False

        stack = []
        closeOpen = {']':'[', ')': '(', '}':'{'}

        for c in s:
            
            # Check if c is in a closing bracket
            # Iterating over a dict is like going over keys
            # Therefore this is check to see if we found an closing in the str
            if c in closeOpen:
                # Update stack if valid pair found
                if stack and stack[-1] == closeOpen[c]:
                    stack.pop()
                
                # Found invalid order of pairs
                else:
                    return False
            # We append opener since we found one
            else:
                stack.append(c)
        
        # At the end the stack must be empty to be a valid parentheses
        return True if not stack else False

        
        
