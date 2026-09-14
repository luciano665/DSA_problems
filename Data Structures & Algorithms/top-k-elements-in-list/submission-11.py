class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # hash map : key=num : val=count of num in nums
        # {3:1, 2:2, 4:3}
        counts = {}
        # An array to store the nums as buckets -> [[], [3], [2], [4]] the index of the list is the freq on which the value isnise list appears in nums
        freq = [[] for i in range(len(nums)+1)] # have buckets for each num in nums

        res = []

        for n in nums:

            counts[n] = 1 + counts.get(n, 0)

        for n, c in counts.items():
            # append the freq of num to correct position on freq-arr
            # Index in freq array tells the freq of num in nums
            freq[c].append(n)

        # Loop in reverse over freq (most freq will be at the end of array)
        for i in range(len(freq) -1, 0, -1):
            # Get value of [[this value]] at index i 
            for num in freq[i]:
                res.append(num)

                # Check if len of res is equal to k
                if len(res) == k:
                    return res
        return []