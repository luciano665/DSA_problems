class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # We init the stack
        stack = []

        # Iterate over lsit of strs
        for c in s:
            stack.append(c)
        
        # Init index 
        i = 0
        
        # While stack is not empty
        while stack:
            s[i] = stack.pop()
            # Update index of list s
            i += 1
