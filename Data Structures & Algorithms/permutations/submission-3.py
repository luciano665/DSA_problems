class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # We will have n! combinations where n is len(nums)
        # We can do this recursively by taking each time the nums[1:]
            # Making the array minus one element each recursive call
        # Until we have no elements left then we return [[]]
        # After that we will have all permutations and posisble indexes to indert to the nums[0]
        # We do this for each permutation and for each index possible in p


        # Base case we got empty list
        if len(nums) == 0:
            return [[]]

        perms = self.permute(nums[1:]) # From index 1 to end
        res = []
        # Need to go over all permutations
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                # Put nums[0] in possible index
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        
        return res
                
                
