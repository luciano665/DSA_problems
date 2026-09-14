class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Init 2 pointers
        l, r = 0, len(s)-1

        # While the pointers have not meet each other
        while l < r:


            # If pointer not equal not palindrome
            if s[l] != s[r]:
                # Skiping left and right chars

                # When skipL the str includes r-char and l+1
                skipL = s[l + 1: r +1]

                # When skipR the str includes l up to r-1(r-alone is noninclusive)
                skipR = s[l:r]

                # Return if equal its reverse str on both cases
                # Will return true if we found a palindrome after remove one element, false otherwise
                return skipL == skipL[::-1] or skipR == skipR[::-1]
            
            # Update pointers
            l, r = l + 1, r - 1
        return True 