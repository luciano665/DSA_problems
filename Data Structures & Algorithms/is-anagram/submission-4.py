class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Will use to hashmaps to keep track of the counts of each char in s/t

        # Base Case lenghts not equal
        if len(s) != len(t):
            return False

        # init hash maps
        hashS, hashT = {}, {}

        # Loop over the str
        for i in range(len(s)):

            # Add key and val+1 (key=char, val=count)
            hashS[s[i]] = 1 + hashS.get(s[i], 0)
            hashT[t[i]] = 1 + hashT.get(t[i], 0)

        # Return T/F if equal hashmaps
        return hashS == hashT
        

 


