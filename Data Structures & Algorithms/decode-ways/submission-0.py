class Solution:
    def numDecodings(self, s: str) -> int:
        # All integers have amapping a char to a int
        # We need to retrun all possible decodings of the str of numbers
        # Leading 0 is invalid since the map is from 1-26 (a-z)
        # Decision tree for each possible path of possible comb
        # We will usin DP caching at eac index i the next possible chars to form a combination
        # Top Down appoach
        

        dp = {len(s): 1}

        def dfs(i):
            # If i already beeing cache
            if i in dp:
                return dp[i]
            
            # Not end of str
            if s[i] == "0":
                return 0
            
            # Recursive call i+1
            res = dfs(i+1)
            # Other case recursive cal for i+2
            if (i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456" )):
                res += dfs(i+2)
            # Cache result
            dp[i] = res

            return res
        
        return dfs(0)

