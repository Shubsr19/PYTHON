#To display star pattern 
row=int(input("enter number of rows"))
for i in range(1,row+1,1):
    for j in range(1,i+1):
        print("*",end='')
    print("")
    """output
    enter number of rowa 5
    *
    **
    ***
    ****
    *****
    """