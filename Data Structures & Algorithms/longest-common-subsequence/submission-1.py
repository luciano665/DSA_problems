class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # We need to return thr longes common substring
        # Comparing the char ad break it into more sub problems
        # A 2d grid will be used, for each char in both strings there is s cell
        # We will find longest subsequence between both
        # Bottom-up approach, at each cell we are on a diff subproblem
            # mOving to adject cells
        # If chars match we go diagonally and add 1 on that match cell
        # We go back from bottom and add where the 1 ares top get the overall sum


        # 2d grid
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]


        # Nested loop ieterate 2d grid in reverse order
        for i in range(len(text1) -1, -1, -1):
            for j in range(len(text2) -1, -1, -1):
                # if chars match
                if text1[i] == text2[j]:
                    # 1 + Val at diagonal entry
                    dp[i][j] = 1 + dp[i+1][j+1]
                # Chars dont match
                else:
                    # The max of value at the right and bottom
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])

        # Result wil be at top left of 2d grid
        return dp[0][0]
