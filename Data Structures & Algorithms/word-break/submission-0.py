class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # We need to return if word in dict appears on s if partitioned
        # We will use the dict to check complete words amtch a prefix on the str
        # We will use a DP Bottom-up, starting at last index of s
        # We will word break each single possible word
        # At each index we set dp[i + len(word)] if wird is found in dict from s
        # We will cache all asnwers for each index in dp array
        # dp[0] will have the final result

        # init cache
        dp = [False] * (len(s) + 1)
        # set base case len(s) = True
        dp[len(s)] = True

        # Iterate in reverse over s
        for i in range(len(s)-1, -1, -1):
            # Go over al word in dict for each position i
            for w in wordDict:
                # Check if word macthes portion to w
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                # If we found one wa to world break it we can exit the loop
                # And move on to next index
                if dp[i]:
                    break
        
        return dp[0]

