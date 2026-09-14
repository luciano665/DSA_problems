class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # Init Hashmap to keep count
        count_map = defaultdict(int) # => if key not exist init as = 0

        # Vars to keep track of val to return and maxcount
        res = maxCount = 0

        # Iterate over nums
        for num in nums:
            # Add num in map with count + 1
            count_map[num] += 1
            
            # if oucurrences of num > than maxcount
            # Set result to num and maxcount = number of occurences of current num
            if maxCount < count_map[num]:
                res = num
                maxCount = count_map[num]
        
        # At this point we will have the final result found
        return res

        



