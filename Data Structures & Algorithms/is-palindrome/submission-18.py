class Solution:
    def isPalindrome(self, s: str) -> bool:
        # We will use a twopointer approach
        # We need extra helper nested function ti check if char is alpahnu,
        # Ignore not none-alphanum

        def isAlphaNum(s):

            # Using ordinal function to check char is valid in range
            return (ord('a') <= ord(s) <= ord('z') or
                    ord('A') <= ord(s) <= ord('Z') or
                    ord('0') <= ord(s) <= ord('9'))
        

        # Init left and right pointer
        l = 0
        r = len(s)-1

        while l < r:

            # Check if char at l and r is valid alpha num
            # If is not we skip and ignore it
            while l < r and not isAlphaNum(s[l]):
                l += 1
            
            while l < r and not isAlphaNum(s[r]):
                r -= 1


            if s[l].lower() != s[r].lower():
                return False
            
            # Update pointer
            l += 1
            r -= 1

        # We have traversed all the str and we checked is a valid palindrome
        return True