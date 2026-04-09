def robot_guardian(age,has_id,knows_password):
    if age >= 18 and has_id==True:
        print(True)
    elif knows_password==True:
        print(True)
    else:
        print(False)
age=int(input())
has_id=bool(input())
knows_password=bool(input())
robot_guardian(age,has_id,knows_password)