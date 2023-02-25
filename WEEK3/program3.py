#To find sum of odd numbers 
sum=0
n=int(input("enter any number"))
for i in range (0,n+1):
    if(i%2!=0):
        print(i)
        sum=sum+i
print(sum)
"""
output 
1
3
5
7
9
25
"""