class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # var to keep track of k-vals that are not a val to remove
        k = 0

        for i in range(len(nums)):

            # If nums at i is not equal to val replace put that at positon k
            if nums[i] != val:
                nums[k] = nums[i]
                # Update pointer k + 1
                k +=1
            
        # Return the k-number not being the var 'val'
        return k