class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # We need to return the K-th largest element in sorted array-(large -> small)
        # Use a min heap to store the nums into it
            # During traversal of nums
        # If heap lenght becomes > k we pop the curr smallest element in heap

        heap = []
        # Start filling the min-heap
        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                # Pop smallest num in heap
                heapq.heappop(heap)

        # After that we will have k-th largest at the root of the heap
        return heap[0]

