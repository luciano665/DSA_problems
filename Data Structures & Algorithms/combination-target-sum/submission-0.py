class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:


        # We are gonna use DFS since we need a recursive solution to form the decision tree
        # We will have pointer started at nums[0] and we get 2 desicion 
            # Add [nums[0]] and not add []
            # We go depth left at each and recursively decide until
            # We either have a valid list of nums that sum up to the target or not
    
        # List to store list of valid nums in nums that it's sum is = target
        res = []

        # Cur is for current combiantion
        # Mantain a total of current comnination
        def dfs(i, cur, total):

            # BASE CASE: valid cur combination
            if total == target:
                res.append(cur.copy())
                return 

            # BASE CASE: invalid combination 
            if i >= len(nums) or total > target:
                return

            # Append curr nums[i] to cur comnination list
            cur.append(nums[i])
            # Recursive call
            dfs(i, cur, total + nums[i])
            # Pop element for 2 decision
            cur.pop()
            # Next element nums[i+1]
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res


        