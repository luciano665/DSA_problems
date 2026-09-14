class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # Each time pick largest 2 elements on the heap
        # We can use a max heap to have largest elements at the root of heap
        # After pop the 2 largest elements check contidion for destroying
        # Need to update heap if x < y if equal we break

        # If list is not null
        if not stones:
            return 0
        # Make all elements in list to be its opposite sign
        for i in range(len(stones)):
            stones[i] = -stones[i]

        # Create a max heap
        heapq.heapify(stones)



        while len(stones) > 1:
            # Get 2-largest stones
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)

            # Check conditions
            if abs(x) < abs(y):
                newVal = abs(y) - abs(x)
                heapq.heappush(stones, -newVal)

            elif x == y:
                heapq.heappush(stones, 0)




        
        return -stones[0]
        


        