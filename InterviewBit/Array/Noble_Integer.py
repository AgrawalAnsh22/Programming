class Solution:
	# @param A : list of integers
	# @return an integer
	def solve(self, A):
        A.sort()
        for x in range(0, len(A)):
            if(A[x]==len(A)-1-x):
                if(A[x]==0):
                    return 1
                if(A[x]<A[x+1]):
                    return 1
        return -1