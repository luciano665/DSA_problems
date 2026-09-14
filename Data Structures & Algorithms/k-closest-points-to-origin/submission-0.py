class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # We can use Max-heap that keeps the max distance of the points to the origin at the top
            # With the points as a list
        # We keep poping from ther max heap until we have k-elements on the maxHeap
        # We converts that into list of list and return it

        heap = []

        # Iterating the list
        for x, y in points:
            # Max-heap need to invert the sigh on each dis to haev max at top
            dis = -((x**2) + (y**2))

            heapq.heappush(heap, [dis, x, y])

            # Nedd to have only K most elements in the maxheap
            if len(heap) > k:
                heapq.heappop(heap)

        res = []

        # We have only K elements in the max heap
        # Nedd to coverte the points into a list of list for the result
        while heap:
            dis, x , y = heapq.heappop(heap)
            res.append([x, y])

        return res

        
         