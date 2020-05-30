# Given a positive integer A, return an array of strings with all the integers from 1 to N.
# But for multiples of 3 the array should have “Fizz” instead of the number.
# For the multiples of 5, the array should have “Buzz” instead of the number.
# For numbers which are multiple of 3 and 5 both, the array should have “FizzBuzz” instead of the number.

# Look at the example for more details.

# Example

# A = 5
# Return: [1 2 Fizz 4 Buzz]

# -------------------------
# Solution
# -------------------------

class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
        result=[]
        for x in range(1,A+1):
            if(x%3==0 and x%5==0):
                result.append("FizzBuzz")
            elif(x%3==0):
                result.append("Fizz")
            elif(x%5==0):
                result.append("Buzz")
            else:
                result.append(x)
                
        return result
