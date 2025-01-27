#User function Template for python3
class Solution:
    def printMinNumberForPattern(ob,S):
        # code here 
        stack = []
        res = ''
        
        for i in range(len(S) + 1):
            stack.append(i + 1)
            
            if (i == len(S) or S[i] == 'I'):
                while len(stack) > 0:
                    res += str(stack.pop())

        return res