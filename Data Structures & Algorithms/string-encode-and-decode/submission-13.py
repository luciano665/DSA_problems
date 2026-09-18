class Solution:

    def encode(self, strs: List[str]) -> str:

        # Store the len of str at first 
        # Then add delimiter to specidfu satrt of actual strs to edecode later

        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:


        # We need smart way to move to point to corrent indexes
        # WHile decoding
        res = []
        l = 0

        while l < len(s):

            # init r pointer
            r = l

            while s[r] != '#':
                # each time we need to put r into # to get length
                r += 1 

            # get len of str to decode
            length = int(s[l:r])

            # Update pointers

            l = r +1 #start of str to decode
            r = l + length # next lenght of next str to decode

            res.append(s[l:r])

            # Reset pointer to correct idx for next str to decode
            l = r # curr length of next str 

        
        return res

