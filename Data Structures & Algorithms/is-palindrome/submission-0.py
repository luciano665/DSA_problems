class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Reverse string approach

        # New str init
        new_str = ''
        
        #Iterate over chars in s
        for c in s:
            # Checks if is alfanumeric
            if c.isalnum():
                
                # Append char to new string
                new_str += c.lower()
        
        # Return bool if new_str equals it'reverse
        return new_str == new_str[::-1] #-> syntax for reverse string
        