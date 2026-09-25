class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # So we do need slisind window approach
        # Bc we need logest-seq of repeed chars with at most k changes
        # Each char in s will be target to be logest samer char -seq
        # Must iterat over set to look fo each possible target to find the longest
        # We will use  pointer where r expands the window and l shrinks it
        # In order to know that we execeede k is the diff on len of current window and curr freq


        res = 0
        chars = set(s)

        for c in chars:

            # Init the count for target c and lpointer
            count = 0
            l = 0

            # Start the window no for each possible c over s
            for r in range(len(s)):

                # Update freq-count if faound vlaid char
                if s[r] == c:
                    count += 1

                # We must ensure each time we do exceed k to shirnk window
                while (r - l + 1) - count > k:
                    # Reduce frequency count
                    if s[l] == c:
                        count -= 1
                    
                    # shrink window
                    l += 1

                res = max((r-l+1), res)
        return res


                

