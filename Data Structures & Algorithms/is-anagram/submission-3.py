class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Will use to hashmaps to keep track of the counts of each char in s/t

        # Base case length not equal 
        if len(s) != len(t):
            return False 
        hashS, hashT = {}, {}

        for i in range(len(t)):

            # +1 to vals to curren char(key)
            hashS[s[i]] = 1 + hashS.get(s[i], 0)
            hashT[t[i]] = 1 + hashT.get(t[i], 0)

        # Compare both hashMaps 
        return hashS == hashT
 


