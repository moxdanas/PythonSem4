marks1 = int(input("Enter Num:"))
marks2 = int(input("Enter Num:"))
marks3 = int(input("Enter Num:"))
average = (marks1+marks2+marks3)/3
if(marks1<33 or marks2<33 or marks3 < 33  ):
    print("failed !")
elif (average<40):
    print("failed !")
else:
    print("Passed!")