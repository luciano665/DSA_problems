class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # We must return all possible combinations of cadidates that sum up to target
        # This time you can not re-use a cadidate n times
        # You can only use an element multiple times only if shows ups 
            # N multiple times on the list of cadidates
        # Also we can have duplicate combinations

        # We will sort the list to have all multiple elemts group togheter
        # Also inside DFS we will have a loop to shift pointer if next equals prev elem on list

        res = []
        candidates.sort()

        def dfs(i, cur, total):

            # Base case when we have valid combination
            if total == target:
                res.append(cur.copy())
                return

            # Base cas if total > targert or i outOFbonds
            if total > target or i == len(candidates):
                return

            
            # 1st deci: Include cadidates[i]
            cur.append(candidates[i])
            #Can not reuse cadidate at idx i
            dfs(i+1, cur, total + candidates[i])
            
            # 2nd deci: skip candiates[i]
            cur.pop() # from prev step
            
            # ex; [1, 1, 1, 1, 2, ...] -> want to skip all 1's
            # On the path above we already include all 1's
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            
            # i ends up at the last element that appeard multiple times on list
                # Need to pas i+1
            dfs(i + 1, cur, total)


        dfs(0, [], 0)
        return res


