#To print the biggest number by comparing three variables
a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)
"""output
enter first number 30 
enter second number 7
enter third number 22
30
"""