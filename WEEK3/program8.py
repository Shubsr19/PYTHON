#to display numbers in half pyramid form
row=int(input("enter number of rows"))
for i in range(1,row+1,1):
    for j in range(1,i+1):
        print(j,end='')
    print("")
    """
    enter number of rows 5
    1
    12
    123
    1234
    12345
    """