class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # We need to return T if s1 and s2 can from s3
        # Relvative order of char on string is a must
        # We will use a DP approach using caching
        # we wil have 2 pointer one for each s1 and s2 when traversing them
        # The psotion (x,y) is pointer at index x of s1 and index y of s2
        # We traverse s3 and s1,s2 and compre each index at s1 and s2 at current s3
        # we have grid that each row is s1 char and each col is s2 chars, plus extra layer
        # Base case is when out if bound from pointer on s1,s2, s3 we form valid s3
        # We compute index on s3 from s1s2 by adding index from curr s1 and s2
        

        # Base case: len(s1 + s2) equal s3 -> True
        if len(s1) + len(s2) != len(s3):
            return False
        
        # Init entire 2D-DP grid to False 
        dp = [[False]* (len(s2) + 1) for i in range(len(s1) + 1)]

        # Out of boud positon on s1 and s2 set to true
        dp[len(s1)][len(s2)] = True

        # We start at bottom right corner and go way up
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):

                # If current chars are in bounds and mactch target
                # and result of dp is True
                # We set in dp grid to true
                # dp[i+1][j] checks that the rest of the suffix s3[i+j+1:] 
                    #can be built from s1[i+1:] and s2[j:]
                if i < len(s1) and s1[i] == s3[i + j] and dp[i+1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j+1]:
                    dp[i][j] = True

        
        # Return dp[0][0] which has result
        return dp[0][0]


        