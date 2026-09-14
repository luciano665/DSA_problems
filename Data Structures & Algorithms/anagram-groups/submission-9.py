class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # We will use a hash map
        # Mapping count of chars to list of strs

        res = defaultdict(list)

        # Must iterate over the str
        for s in strs:

            # We need to init and array of 26 (a..z) with all 0s
            count = [0] * 26

            # Iterate over current str
            for c in s:

                # We put the counts for each str
                count[ord(c) - ord('a')]  += 1# since if s is 'a' -> count[26-26=0] += 1

                # We must appedn that count into hasmap
            res[tuple(count)].append(s)

        # Return the values that are a list of lists
        return list(res.values())