class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # We first init out str as empty
        res = ""

        # We want to iterate over the first string
        # We choose the first arbitrary (shortest str, may or may not -> edge case)
        for i in range(len(strs[0])):  # i = 0, 1, 2 …

            # Get over all strings in the list
            for s in strs:

                # We check the string s at index i to the first string at index i
                # If equal we continue
                if i == len(s) or s[i] != strs[0][i]:
                    return res
                    
            # Add char to result
            res += strs[0][i]
        
        # Return res
        return res


        