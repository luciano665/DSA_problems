class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # We will a slidding window appaorch with 2 pointer
        # Array is sorted in increasing order
        # So small elemts on th eleft and big on right
        # Index1 and index 2 sum up to target 
        # if sum is greater we decrease right pointer 
        # If sum less increase left pointer

        l = 0
        r = len(numbers)-1

        while l < r:

            currSum = numbers[l] + numbers[r]

            if currSum > target:
                r -= 1

            elif currSum < target:
                l += 1
            
            else:
                return [l+1, r+1]
        
        return []

            