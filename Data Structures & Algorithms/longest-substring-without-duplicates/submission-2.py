class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # We will use a slicing window approach 
        # With two boundries L and R
        # The length of the max length of window is the result
        # Update L pointer if R ointer is a pointing to char already in set
        # Loop over string using R pointer
        # Must check if char at R is in set -> if so remove char at L and move L-bound+1
            # Update window
        # We add R elemenet into set if it was not there
        # Take the max of the window -> compare curen maxL and new length computed
        # Computer new length of window -> R-bound - L-bound + 1 (zero indexed)
        # After loop return maxL var

        # Vars
        maxL = 0
        l = 0
        charSet = set()

        for r in range(len(s)):
            # Must remove elements that are not in window
            while s[r] in charSet:
                # Remove L bc that R is in the set
                charSet.remove(s[l])
                # Update L pointer
                l += 1

            # Add element to set if is not there
            charSet.add(s[r])
            maxL = max(maxL, r-l+1)

        return maxL


        




