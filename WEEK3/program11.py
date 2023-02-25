#To count the total number of digits using while loop 
x=int(input("enter number"))
count=0
while x!=0:
    x=x//10
    count=count+1
print(count) 
"""output
enter number 30040
5
"""