class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # hash map : key=num : val=count of num in nums
        # {3:1, 2:2, 4:3}
        # We need a dict for counts 
        # Need list of list for buckets to store freq of num in nums
        # Index of the list will be the freq of num at that index in nums
        # Need empry array of to store result

        counts = {}
        # Array freq must be (0...len(nums) +1) since is zero index and a num can appear len(nums)
        freq = [[] for i in range(len(nums) + 1)]

        res = []

        # Fill up dict of counts
        for n in nums:
            counts[n] = 1 + counts.get(n,0)

        # Fill up the freq array 
        # where the value in buckets is the num at index=frequency
        for v, c in counts.items():
            freq[c].append(v)

        # Loop in reverse free since last bucket in freq is the most frek elemen
        for i in range(len(freq)-1, 0, -1):
            # Get the num at freq[i]=bucket at index i = freq[i] appears i-times in nums
            for num in freq[i]:
                # Append num into res (last=most-freq)
                res.append(num)

                # Check if curren res-length == k
                if len(res) == k:
                    return res