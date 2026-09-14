class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # Two pointer solution
        # Init array to store triplets
        # Sort array (small -> large)
        # We will loop over enumerate nums (i, n)
        # To get sum of triplet that = 0
        # Set 0 elem of list as first elem of triplet
        # L and R pointers: L = i+1, and R = len(lst)-1
        # Set loop condition while l < r 
        # Get three sum candidate
        # Update L++ pointer if sum < 0 and R-- pointer if sum > 0
        # Else add triplet into result and update pointers
        # Must skip duplicates of triplets 
            # Check curr val of loop is not equal to past val on past iter
            # And same for L-pointer after triplet is found keep L++ until no duplicate
        
        # Init:

        res = []
        nums.sort()

        # Init loop for
        for i, n in enumerate(nums):

            # Check if n > 0 break since there is no comb that = 0
            if n > 0:
                break
            
            # Continue if curr val of n is equal to past after 1-iter
            if i > 0 and n == nums[i-1]:
                continue # do next iter of loop

            # Init pointers
            l = i + 1
            r = len(nums) - 1

            # Loop to get 2nd and 3rd candiated for sum
            while l < r:
                # Get three sum
                threeSum = n + nums[l] + nums [r]

                # Update pointers
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                # Else we found a triplet and we update pointers
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # Skip left duplicates since we dont want to form same triplet
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res