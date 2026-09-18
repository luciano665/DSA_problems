class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # base case lan missmatch
        if len(s) != len(t):
            return False

        
        # 2 hasmaps neede to stores key-val pairs
        hashS = {}
        hashT = {}

        # Iterate over str len not actual
        for i in range(len(s)):
            # Populate both hasmaps with char ans counts
            # Get the key at current char
            hashS[s[i]] = hashS.get(s[i], 0) + 1
            hashT[t[i]] = hashT.get(t[i], 0) + 1
        
        # iterate over the a hashmap already populated
        for c in hashS:
            if hashS[c] != hashT.get(c, 0):
                return False
        
        return True
