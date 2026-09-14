class Solution:
    def countSubstrings(self, s: str) -> int:
        # We need to return the number of all possible palindromes substrings
        # A single char counts as a palindrome
        # We are going to expan from each positon to both sides
        # L and R start at first char and move outwards
        # Update count if palindrome was found
        # At each char we expand as much as we can until we go out of bounda
        # For even length substr we need to start at even position 
        # For we start at the begging of str


        res = 0

        for i in range(len(s)):
            # Init odd pointer
            l,r = i, i
            
            # While pointer are in bounds and match curr char
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # Update pointer and result
                res += 1
                l -= 1
                r += 1
            
            # Init for even lengths pointer 
            l, r = i, i+1
            # While pointer are in bounds and match curr char
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # Update pointers and res count
                res += 1
                l -= 1
                r += 1
            
        return res