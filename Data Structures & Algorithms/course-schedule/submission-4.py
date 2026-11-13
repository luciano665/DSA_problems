class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # We need to represent the problem as graph problem
        # Where each node a is course and its prerequisite is an edge
        # In order to return valid completness of courses we need to be able to detect a cycle
        # If a cycle is found then we return false
        # We need hashset for each DFS call in order to detect cycle
        # If current path nocde is in hash then we now there is a cycle
        # After each course (key) is travese (path) we put its list a empty
            # Such that its marked as done
        
        
        # Need to first build the dict (adj list)
        preMap = {i: [] for i in range(numCourses)}
        for crs, preq in prerequisites:
            preMap[crs].append(preq)
        

        # Set to keep track of paths
        visited = set()

        def dfs(crs):

            if crs in visited:
                # cycle here
                return False

            # We must check first if this course has prere (empty list)
            if preMap[crs] == []:
                # Valid completness course is done
                return True
            
            # We add this crs current path
            visited.add(crs)
            
            # We need to keep travesing its prereq
            for pre in preMap[crs]:
                # Check if cycle
                if not dfs(pre):
                    return False
                
            # There no cycles in this course course
            # need to remove the crs from set 
            visited.remove(crs)

            # Markeed current course as done
            preMap[crs] = []
            return True
        
        # outer loop for traversing each course
        # Since we have total of numcourses (where key is the number)
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        # Else valid prereq
        return True
