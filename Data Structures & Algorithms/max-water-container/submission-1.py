class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # Use two pointer solution
        # L and R pointer where R is at the end and L at idx 0
        # Init var to store max amoun of water
        # Area=l*w - > l = R - L and w = min(num at L, num at R)
        # We then get the max of current max amourn of water and recently area calculated
        # We update L++; if num at L < num at R else: R--

        # Init var and pointer
        res = 0

        l = 0
        r = len(heights) - 1

        # Loop array 
        while l < r:
            # Compute area
            area = (r-l) * min(heights[l], heights[r])
            # Update res
            res = max(res, area)

            # Update pointers
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return res