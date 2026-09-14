class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Init en mepty set
        n = set()

        for num in nums:
            if num in n:
                return True

            n.add(num)
        return False

        