# Given an integer n, return the number of trailing zeroes in n!.

# Note: Your solution should be in logarithmic time complexity.

# Example :

# n = 5
# n! = 120 
# Number of trailing zeros = 1
# So, return 1

class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        fives=A//5
        temp=fives//5
        while(temp>0):
            fives=fives+temp
            temp=temp//5
        return fives