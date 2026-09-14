class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # We can use a max-heap to keep the most freq task at the top
        # We need a queue such that when pop from heap we enque te value,time where it can added again to the heap
        # We global var to kepp track of time
        # We return this time var as the min time to schedule all task


        heap = []
        queue = deque()
        counter = collections.Counter(tasks)
        t = 0 

        # We iterate over the map of freq of counter to create heap

        for v, fr in counter.items():
            # Populate the max-heap
            heapq.heappush(heap, -fr)


        # Start the task scheduling
        while heap or queue:
            # Update timer
            t += 1

            if not heap:
                time = queue[0][1]

            # Pop next task from heap
            else:
                task = 1 + heapq.heappop(heap)

                # Add curr task to queue with idle
                if task:
                    queue.append([task, t+n])

            if queue and t == queue[0][1]:
                heapq.heappush(heap, queue.popleft()[0])

        return t

            


