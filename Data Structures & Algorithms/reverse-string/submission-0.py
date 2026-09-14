class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # We init two pointer
        # One pointing a the beginning of array and one at teh end
        l, r = 0, len(s) -1

        # While left pointer is less right one; moving -> <-
        while l < r:
            # Swap of values 
            s[l], s[r] = s[r], s[l]
            # Update pointers
            l += 1
            r -= 1
            