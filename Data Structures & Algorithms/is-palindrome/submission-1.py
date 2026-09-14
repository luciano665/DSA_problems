class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Init pointers
        l, r = 0, len(s) - 1


        while l < r:
            # If L-pointer is not alphanumeric
            while l < r and not self.alphaNum(s[l]):

                # Increment pointer
                l += 1
            
            # If R-pointer is not alphanumeric
            while r > l and not self.alphaNum(s[r]):

                # Decrement pointer
                r -= 1
            
            # If not equal, is not a palindrome
            if s[l].lower() != s[r].lower():
                return False
                
            # Else update pointer, current pointers match
            l, r = l + 1, r - 1
        return True
    

    def alphaNum(self, c):
        # Check the ASCII value of current char/element in str
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))