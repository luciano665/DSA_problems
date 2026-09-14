class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Must return the number of wasy we can get the target from the nums
        # We must keep track of the postion we are at
        # We will soleve it using memoization

        # DP structure
        dp = [defaultdict(int) for _ in range(len(nums) + 1)]

        dp[0][0] = 1 # (0 elements, 0 sum) -> way
                    # 1 way to sum to 0 with first 0 elements
        
        # Iter over nums and current grid 
        for i in range(len(nums)):
            for  cur_sum, count in dp[i].items():
                # 2 coices we either + or -, at that position
                dp[i + 1][cur_sum + nums[i]] += count 
                dp[i + 1][cur_sum - nums[i]] += count
        
        return dp[len(nums)][target]