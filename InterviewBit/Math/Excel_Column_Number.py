# Given a column title as appears in an Excel sheet, return its corresponding column number.

# Example:

#     A -> 1
    
#     B -> 2
    
#     C -> 3
    
#     ...
    
#     Z -> 26
    
#     AA -> 27
    
#     AB -> 28 

class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        result=0
        for x in range(len(A)):
            result*=26
            result+=ord(A[x])-ord('A')+1
        return result
        