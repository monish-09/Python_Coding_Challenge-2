#question2 program to classify the user as minor,adult or minor
age = int(input("enter the age: "))
if(age<18):
    print("Minor")
elif(18<=age<25):
    print("Adult")
else:
    print("Senior")