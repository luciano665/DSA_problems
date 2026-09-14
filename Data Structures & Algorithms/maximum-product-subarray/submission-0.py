class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Need to return continuos max subarray product (at least one element in subarray)
        # Brute Force: divide array into n subarrays and compute product of each sub array at each element
            # Not efficient at all -> n (subarrays) * n (elemnets)
        # Must watch out on negative adn possible avls in nums
        # If all positive product increases if all negative (sign alternates)
        # Need to keep track of min and max of product of subarray
        # If 0 appeara set min and max to 1 ro not kill product

        res = max(nums) # not zero

        curMin, curMax = 1, 1
        
        # Iter over nums
        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            # Temp to store prev curMax*n 
            temp = n * curMax
            # Recompute curMin/Max
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(temp, n * curMin, n)
            #Update res for max
            res = max(res, curMax)
        
        return res
