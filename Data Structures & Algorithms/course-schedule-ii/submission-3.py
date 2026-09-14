class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # We need a hashmap for the course and its pre-req
        # We will use DFS to traverse the a valid path
        # Inside the DFS we need to build a list on wich the valid path on 
            # how to the take courses (order)

        # Init map
        hashMap = {i: [] for i in range(numCourses)}

        # Populate the pre-req for each course
        for crs, pre in prerequisites:
            hashMap[crs].append(pre)

        # Visited courses set
        cycle = set()
        visit = set()


        # list to return
        res = []

        # Helper dfs func
        def dfs(crs):

            # Base cases

            # Course already visited
            if crs in cycle:
                # Cycle detected
                return False
            # If course was visited before
            if crs in visit:
                return True
            
            # Add curr course to cycle set to detect if cycle
            cycle.add(crs)
            for pre in hashMap[crs]:
                # Invalid graph cycle on pre-req
                if not dfs(pre):
                    return False
            # Valid schedule
            cycle.remove(crs)
            # Current visit
            visit.add(crs)
            res.append(crs)
            return True

        # Need to do that over all courses
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        # Return thr valid path
        return res



            