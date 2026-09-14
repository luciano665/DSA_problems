class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Create a set to add elements into it
        hash_set = set()

        # Iterate over nums and add them into set if not in set before
        for n in nums:
            if n not in hash_set:
                hash_set.add(n)
            else:
                return True
        
        # If no duplicates return False
        return False

        
        