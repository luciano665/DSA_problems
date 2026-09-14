class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Palidrome: str thar reads the same forward and backwards.
        # AlphaNum: (A-Z, a-z) and (0-9)

        # We will use a two pointer approach one of the left and other at the right
        # Loop over str and chec pointers
        # Increment L pointer if curr char is not alphanum and L < R
        # Decrement R pointer if curr char is not alphanum and L < R
        # Final check if L!=R -> return False
        # Must update pointers to next char of str after check
        # Exit loop means is valid palidorme -> return True
        # Need a helper functiont to check is char is alphanum
        # If helper return False -> char is not valid alphanum

        # pointers
        l = 0
        r = len(s) - 1
        
        # Init loop
        while l < r:

            # Increment L-pointer if is not alpahNum by L++ and l < r
            while l < r and not self.isAlphaNum(s[l]):
                l += 1
            
            # Decrement R-pointer if is not alphaNum R-- and r > l
            while r > l and not self.isAlphaNum(s[r]):
                r -= 1
            
            # Check current pointer if not equal (all lower case)-> R False
            if s[l].lower() != s[r].lower():
                return False

            # Updater of pointer since both l and r chars are equal -> move on
            l = l + 1
            r = r - 1

        
        # If we exit loop is valid palidrome
        return True


    
    # Helper function to check current char is alphanum
    def isAlphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
        ord('a') <= ord(c) <= ord('z') or
        ord('0') <= ord(c) <= ord('9'))

        