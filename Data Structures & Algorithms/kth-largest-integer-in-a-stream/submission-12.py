class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # Init array as min-heap with nums
        self.heap = nums
        heapq.heapify(self.heap)

        # Have the min heap with the k-th largest elements
        while len(self.heap) > k:
            heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:

        # Insert the new val into heap
        heapq.heappush(self.heap, val)

        # We still need to have the k-th largest elements on heap
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]
