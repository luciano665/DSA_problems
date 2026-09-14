class Solution:

    def encode(self, strs: List[str]) -> str:
        # Encode string
        res = ""
        for s in strs:
        
            res += str(len(s)) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:

        res = []
        i = 0

        while i < len(s):
            # Init another pointer j = i
            j = i

            # Since we need to get the length of each str "3#abc" -> i=3 and j ="#"
            while s[j] != "#": 

                j += 1

            # Get the length
            length = int(s[i:j]) # where j is exclusive since j point to "#"

            # Update pointer i to point to first char in the str to be dedcode that is j+1
            i = j + 1

            # We need j to be pointing to next length of the next str
            # Since i is pointing to the first char will i =Length
            j = i + length

            # Appedn that str to list
            res.append(s[i:j])

            # Start new decode of str
            i = j # both point length of str to be decoded
        
        return res


            
            
