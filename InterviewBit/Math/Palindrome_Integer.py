# Determine whether an integer is a palindrome. Do this without extra space.

# A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit reversed.
# Negative numbers are not palindromic.

# Example :

# Input : 12121
# Output : True

# Input : 123
# Output : False

class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        p=str(A)
        n=len(p)
        loop=n//2
        if(n==1):
            return 1
        for x in range(0,loop):
            if(p[x]==p[n-1-x]):
                continue
            else:
                return 0
        return 1