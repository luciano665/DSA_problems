class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # Will use a hashMap/set

        hashS = set()

        for n in nums:

            # Check if curr num is in set -> duplicate found
            if n in hashS:
                return True
            
            hashS.add(n)

        # No duplicate found
        return False


    