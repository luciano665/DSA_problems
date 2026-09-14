class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        # Iteration
        conc = []
        for i in range(2):
            for n in nums:
                conc.append(n)
        
        return conc
        