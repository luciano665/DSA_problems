class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Hashmap approach to store key-val pairs
        # Where the key will be an array of lenght 26
        # so we have each index represting a word from a-z
        # The value will be a list each val pait is a group of anagrams
        # Must return this as list of lists

        hashM = defaultdict(list)

        for s in strs:

            count = [0] * 26

            for c in s:

                count[ord(c) - ord("a")] += 1

            hashM[tuple(count)].append(s)

        
        return list(hashM.values())