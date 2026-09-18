class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # We will use hashset to store explored vlaid init sequences
        # Need to go over nums in lis to get valid starting points
        # Will update a valid sequence if founc in hashmap
        # Where the key is the sarting valid num and val is valid sequence
        # Need to return longest sequence leng

        hashset = set(nums)
        longest = 0

        for num in nums:
            
            # Chcek if it an ivalid num to star sequence
            if (num-1) not in hashset:
                # temp var to keep track over curr valid seq length
                curr_long = 1

                # While there num+1 exists we upadte len
                while(num + curr_long) in hashset:
                    # Update curr seq len if valid next num found
                    curr_long += 1

                # update longest based on curr longest and prev longest seq
                longest = max(longest, curr_long)

        
        # return longest valid deq found
        return longest
                
            