class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # We can use a stack to store the tokens that are numbers
        # We use if staments
        # Such that we have the operand as a str
        # Each time we ecounter and operand we pop two numbers from the stack
            # And perform the curren operand
        # If we ecounter a number we pust into the stack


        stack = []

        for t in tokens:

            # Must check which operation we are performing
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "*":
                p1 = stack.pop()
                p2 = stack.pop()
                stack.append((p2 * p1))

            elif t == "-":
                p1 = stack.pop()
                p2 = stack.pop()
                stack.append((p2 - p1))
            elif t == "/":
                p1 = stack.pop()
                p2 = stack.pop()
                stack.append(int((float(p2) / p1)))

            # Encounter number must be push into the stack
            else:
                stack.append(int(t))

            
        # Result of the expression  
        return stack.pop()
