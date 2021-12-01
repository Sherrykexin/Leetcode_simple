class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        my_dict = {')':'(',']':'[','}':'{'}
        for i in s:
          #if it is a open bracket, append to the stack
            if i in my_dict.values():
                stack.append(i)
          #if it is a closed bracket, check if the stacj is empty or there is open bracket for it
            elif i in my_dict.keys():
                if not stack or my_dict[i] != stack.pop():
                    return False
            else:
                return False
        return len(stack) == 0
            
