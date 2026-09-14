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

        l = 0
        r = len(s) - 1

        while l < r:
            
            # Check if pointers are pointing not not alpha nums
            # If so skip non alphanum
            while l < r and not self.isAlphaNum(s[l]):
                l += 1

            while r > l and not self.isAlphaNum(s[r]): 
                r -= 1

            # Final check of not match return false is no palindrome
            if s[l].lower() != s[r].lower():
                return False

            # Update pointer
            l += 1
            r -= 1
        
        #If all was good we return true

        return True


    
    # Helper function to check current char is alphanum
    def isAlphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
        ord('a') <= ord(c) <= ord('z') or
        ord('0') <= ord(c) <= ord('9'))

        