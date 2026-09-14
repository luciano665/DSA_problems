class Solution:
#Design an algorithm that takes 2 main functions encode and decode
#Encode needs to put a list of strs into a single str by using some king of delimiter
#Decode must return the input of the encode funtion
#We will approach this proble by encding each str adding at the beginning the length of it and a #
#That will be add add the begginign of each string we are contanetating into a single string from the [strs]
#So we know how to decoded after
#O(N) time
#O(N) time
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s #ex:'3#code'
        return res   

    def decode(self, s: str) -> List[str]:
        res, i = [], 0 #-> i is apointer to know where position we are at
        
        # i is still in range
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) #i will be tht integer and j the '#' we dont include j just i
            #We add from j + 1(start of str) until teh last char of the str not including the next length of the next str (j + 1 + length)
            res.append(s[j + 1 : j + 1 + length]) # -> 'j+1+length is the actual string, since j is current at #, +1 is the start of teh str
            i = j + 1 + length # -> update i pointer to the next i
        return res