#To check if the person is eligible for ncc or not
a=int(input("enter age"))
b=float(input("enter height"))
c=int(input("enter weight"))
if a>18:
    if b>5.8:
        if c>60:
            print("eligible for ncc")
else:
    print("not eligible")
    """
    ouput
    enter age 20
    enter height 5.9
    enter weight 74
    eligible for ncc
    """
        
