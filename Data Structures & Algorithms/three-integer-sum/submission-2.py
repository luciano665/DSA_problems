class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        
        # Init:
        res = []
        nums.sort()

        for i, n in enumerate(nums):

            # if  a > 0 break
            if n > 0 :
                break

            # We don't want to form same triplet
            if i > 0 and n == nums[i-1]:
                continue

            # Init pointer to be i+1 and last element i nums
            l = i +1
            r = len(nums) -1

            while l < r:

                # Compute the sum
                sumT = n + nums[l] + nums[r]

                # We know if sum < 0 we need bigger L and vicerversa for if sum > 0 for R
                if sumT < 0:
                    l += 1
                elif sumT > 0:
                    r -= 1

                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # We must check if L or R are nto the same as before if so must move one
                    while l < r and nums[l] == nums[l-1]:

                        l += 1

        return res

        