class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # We will use  hash set and a sliding window approach
        # Iterate over chars in s by moving r pointer and updating set
        # Each time we check if we duplicat in set if is present on curr window
        # If so we shrink the window and at each iteration we update max length based on window

        hashS = set()
        l = 0
        maxLen = 0

        for r, c in enumerate(s):

            # Check if char is in set
            # If so we remove duplicates
            while c in hashS:
                hashS.remove(s[l])
                l += 1

            # If not a duplicate
            hashS.add(c)

            # Update current max lenght based on windows length
            maxLen = max(maxLen, r - l + 1)
        
        # After the for loop we will have in maxLen the longest subtring in s 
        # With no duplicates
        return maxLen
