# Reverse digits of an integer.

# Example1:

# x = 123,

# return 321
# Example2:

# x = -123,

# return -321

# Return 0 if the result overflows and does not fit in a 32 bit signed integer

class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        num=0
        x=0
        if(A<0):
            A=A*(-1)
            x=1
        while(A>0):
            new=A%10
            num=num*10+new
            A=A//10
        if(x==1):
            num=num*(-1)
        if (num >= 2147483647 or num <= -2147483648): 
            num = 0
        return num