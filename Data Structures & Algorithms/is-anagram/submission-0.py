class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # We will have to hashmaps for keepint track of the 2-strs
        # First we check if len are equals of not they are not anagram

        if len(s) != len(t):
            return False
        
        # Create Hashmaps for both strs
        countS, countT = {}, {}

        for i in range(len(t)):

            # Add count if char i by 1 if nt in hashmap for both strings
            countS[s[i]] = 1 + countS.get(s[i], 0)
            
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # Second loop to check if both hashmaps are equal if so they valid anagram
        for c in countS:
            # Get current count of char c in dicts and if not equal no Valid anagram
            if countS[c] != countT.get(c, 0):
                return False
        
        # If all counts are equal there is a valid anagram
        return True

