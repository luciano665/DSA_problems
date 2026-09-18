class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # We will a bucket sort approach
        # We will a list of buckets where each idx is count of freq
        # Use hashm to store the freq for ach element on nums

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        res = []

        # Iterate over nums
        for num in nums:

            count[num] = 1 + count.get(num, 0)

        # Loop over the count items to be added to the freq list
        for n, i in count.items():
            freq[i].append(n)

        # Lopp over in reverse order over freq
        for i in range(len(freq)-1, 0, -1):

            # Iterate over that curr bucket
            for num in freq[i]:
                res.append(num)

                if len(res) == k:
                    return res



