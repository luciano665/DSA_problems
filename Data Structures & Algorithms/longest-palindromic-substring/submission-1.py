class Solution:
    def longestPalindrome(self, s: str) -> str:
        # We need to get a valid palidrome from substr of a str
        # We will start from the middle char and expand outwards and then,
            # Check each side char and compare if equal palidrome
        # Need to find longest palindrome
        # Edge case even a palindrome 

        res = ""
        resLen = 0

        # Go over each char in string
        # Considerig each as the ceter, where we will expand from it
        for i in range(len(s)):
            # Odd length palidromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # Check if we found a longest subStr
                if (r-l +1) > resLen:
                    # Update result with curr valid palindrome
                    res = s[l:r+1]
                    # Update current palindorme substr length 
                    resLen = r-l+1
                
                # Update pointer
                l -= 1 # left shift
                r += 1 # right shift
            # Even length
            l , r = i , i+1
            # We check the same as for odd length
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    res = s[l: r+1]
                    resLen = r-l+1
                l -= 1
                r += 1
        
        return res




