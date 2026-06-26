class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for i in tokens:
            print(stack)
            if ((i.lstrip("-")).isdigit()):
                stack.append(int(i))
                continue
            
            if(i == "+"):
                stack.append(stack.pop() + stack.pop())
            elif(i == "*"):
                stack.append(stack.pop() * stack.pop())
            elif(i == "-"):
                stack.append(stack.pop(-2) - stack.pop())
            else:
                stack.append(int(stack.pop(-2) / stack.pop()))

        return stack[-1]