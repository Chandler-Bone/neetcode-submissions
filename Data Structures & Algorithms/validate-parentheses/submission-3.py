class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 == 1:
            return False

        #([{}{[]}])

        s_stack = []

        closeToOpen = {"]":"[", ")":"(", "}":"{"}

        for i in s:
            print(s_stack)
            if i not in closeToOpen:
                s_stack.append(i)
                continue

            if(not bool(s_stack)):
                return False      

            item = s_stack.pop()
            
            if item != closeToOpen[i]:
                return False


        if(not bool(s_stack)):
                return True    
        return False