def secret_door(a1,a2,a3):
    if a1==True and a2==True and a3==True:
        print(True)
    elif a1==True and a3==True:
        print(True)
    elif a2==True and a1==True or a3==True:
        print(True)
    else:
        print(False)
    

a1=bool(input())
a2=bool(input())
a3=bool(input())
secret_door(a1,a2,a3)