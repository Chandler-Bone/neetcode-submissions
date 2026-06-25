class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 == 1:
            return False

        #([{}{[]}])

        s_stack = []

        for i in s:
            if(i == "(") or \
                (i == "[") or \
                (i == "{"):
                s_stack.append(i)
                continue

            if(not bool(s_stack)):
                return False      

            item = s_stack.pop()
            
            if(i == ")") and ("(" != item):
                return False
            if(i == "]") and ("[" != item):
                return False
            if(i == "}") and ("{" != item):
                return False


        if(not bool(s_stack)):
                return True    
        return False