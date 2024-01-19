'''
Includes conditional statements and loops, along with the standard library’s math module and factorial function in order to evaluate the ‘number of combinations’
equation used to generate the values in the triangle.

Number of combinations via "n choose k" or nCk = n! / [k! * (n-k)!]
'''

from math import factorial


def pascal_triangle(n):
   for i in range(n):
       for j in range(n-i+1):
           print(end=' ')

       for j in range(i+1):
          
           print(factorial(i)//(factorial(j)*factorial(i-j)), end=' ')

       print()


if __name__ == '__main__':
   pascal_triangle(5)
