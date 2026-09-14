class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        # We solve this by using hashMap {cours: [pre-req]}
        # We will have a set of all courses along current DFS path
        # During DFS we will add curr course to set and go over its pre-r courses list
        # If they are valid (no cycle detected) we removed it from set and set its pre-r to empty list
        # Need to handle inside DFS when is Truea and when is false

        prevMap = {i: [] for i in range(numCourses)}

        # Populate the hahmap
        for crs, pre in prerequisites:
            prevMap[crs].append(pre)

        # Init the set
        visited = set()

        # DFS func
        def dfs(crs):

            # Base cases:

            # If current crs is in visited there is a cycle
            if crs in visited: 
                return False

            # If the Path is valid return True
            if prevMap[crs] == []:
                return True

            # Need to go over all pre-req of curr crs
            visited.add(crs)
            for pre in prevMap[crs]:
                # Run path in current pre-req
                if not dfs(pre):
                    # Cycle was detected
                    return False
            # No cycle on pre-re courses for crs
            # Upadate set and pre-req courses of curr crs
            visited.remove(crs)
            prevMap[crs] = []
            return True


        # Need to run dfs on all courses
        for crs in range(numCourses):
            # If cycle was detetecd trying to complete courses
            if not dfs(crs):
                return False
        return True