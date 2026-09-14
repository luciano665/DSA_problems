class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Anagram = strs that have same # of chars -> [act, cat]
        # We will use a hash map
        # Mapping count of chars to list of strs

        res = defaultdict(list) # dict of list -> {key=(...): val=[....]}

        # First we must iterate over strs
        for s in strs:

            # Init arrasy of l-26 to get count of chars (a...z)
            # a is index 0 and z is 25
            # Init as a list of zeros
            count = [0] * 26

            # Must iterate over current str chars
            for c in s:

                # Must get count of chars of current str using ascii
                count[ord(c) - ord('a')] += 1 # -> if c = a ASCII IS 26-> COUNT[26-26=0] +1 ; correct index of char 'a'
            
            # Append str to correct key count in dict
            # Must convert count into tuple to accept as a key
            res[tuple(count)].append(s)

        # We return a list of lists -> values of dict
        return list(res.values())


