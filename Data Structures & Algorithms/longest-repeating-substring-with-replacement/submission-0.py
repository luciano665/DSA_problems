class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # We need to return the longest substring of same chars in upper case
        # We can perform at most k changes int he string chars
        # We want to replace the character that is most frequent in the substring in a particular window
        # Use a hashmap to kep count of frequency of chars in substring
        # We compute the windowlwn - count[char] = # of chars we need to replace <= K (window is valid)
            # In order to match the substring to be a single char

        chars = set(s)
        res = 0

        for c in chars:
            count = 0
            l = 0

            # Loop over the current with the R-pointer
            for r in range(len(s)):

                # check if char at r == c
                if s[r] == c:
                    count += 1

                # condition to check if we exceed to k changes we can
                # If so we must shrink the window
                # If length of w > k -> we shrink
                while (r-l+1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                
                res = max(res, r-l+1)
        return res