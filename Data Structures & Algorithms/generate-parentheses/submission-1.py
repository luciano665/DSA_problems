class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # We add a '(' if openC < n
        # We add a ')' if closeC < openC
        # Valif parentheses iff n == openC == closeC

        # Init stack and res lis
        stack = []
        res = []

        def backtracking(openC, closeC):

            # Valid parenthesis
            if openC == closeC == n:
                return res.append(("".join(stack)))

            if openC < n:
                # Add (
                stack.append("(")
                #recursive call openC++
                backtracking(openC+1, closeC)
                stack.pop() # undo operation at each recursive call

            if closeC < openC:
                # add ) to stack
                stack.append(")")
                # recursive call on closeC++
                backtracking(openC, closeC+1)
                stack.pop()

        backtracking(0, 0)
        return res
                     
        