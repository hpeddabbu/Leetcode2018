class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        
        s= list(s)
        if not s:
            return true
        for each in s:
            if s.count(each)==2:
                return true
        """
        stack=[]
        for i in s:
            if i == '(' or i=='[' or i== '{':
                stack.append(i)
            else:
                if not stack or {')':'(' , ']':'[' , '}':'{' }[i]!= stack[-1]:
                    return False
                stack.pop()
        return not stack 
        