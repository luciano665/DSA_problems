class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # We are give a string of o digiste 2-9 inclusive
        # Each digit maps to 3 characters
        # We nned to return all posible combinations of this chars
        # We have 4^n combinations we can actually have, since 4 maps to 3 digits only 89 the rest is 3
        # We will use a hasp map to store the mappinf of chars to each digit (2-9)
        # We first take the first char of str and get all possible chars it maps to
        # The next level of the tree will be the next char and so on 
        # Then we backtrack from the leaves to go up and forming the combinatios

        res = []

        hashMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        # Helper backtrack func, i tells us where char we at in digits
        def backtrack(i, curStr):
            # Base: case we got one current combinations
            if len(curStr) == len(digits): # -> Meaning we have every single char mapped to a digit
                res.append(curStr)
                return
            
            # Iterate over the chars of the str of digits[i], 
            # by mapping each digits[i] to its str of chars
            for c in hashMap[digits[i]]:

                # Recursive call to form the tree (combiations)
                # It forms each path first (not level by level)
                backtrack(i + 1, curStr + c)
            
        # Cheks if digits is not empty
        if digits:
            backtrack(0, "")
        
        return res