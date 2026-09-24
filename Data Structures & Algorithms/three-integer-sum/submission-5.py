class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # So we need to return all triplets that sum up to 0
        # Can not have duplicate triplets
        # We will first sort the arry
        # Start iterating over nums idx i
        # We set 2 pointers (sliding windows) at i + 1 and len(lsit)-1
        # We sum the triplets and check if sum > target decreas r
        # if sum < target decrease L
        # We must amke sure we do not have duplicates 

        res = []
        nums.sort()

        for i, n in enumerate(nums):

            # Only positve values left cna sum up to 0
            if n > 0:
                break

            # Ensure we dont do duplicates triplets
            if i > 0 and n == nums[i-1]:
                continue
            
            # Init pointer l = i+1 and r last num in nums
            l = i + 1
            r = len(nums)-1

            while l < r:
                currSum = n + nums[l] + nums[r]

                if currSum < 0:
                    l += 1
                elif currSum > 0:
                    r -= 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # Ensure no duplicates number again
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        
        return res
