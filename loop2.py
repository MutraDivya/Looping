'''
Write a program to determine whether 'n' is a factorial number or not. Factorial of a number is the product of all positive numbers from 1 to 'n'.
Input format:
The input containing an integer 'n' which denotes the given number.
Output format:
If the given number is factorial, print "Yes". Otherwise, print "No".
Refer the sample output for formatting.
Sample Input:
6
Sample Output:
Yes
'''

def isFactorial(n) :
    i = 1
    while(True) :
        
        if (n % i == 0) :
            n //= i
            
        else :
            break 
            
        i += 1

    if (n == 1) :
        return True 
    
    else :
        return False 

# Driver Code 
if __name__ == "__main__" : 
    n = int(input())
    ans = isFactorial(n)
    
    if (ans == 1) :
        print("Yes") 

    else :
        print("No")
