#create a marksheet

score = list(map(int,input("enter all score :").split(" ")))

print(score)

s = "You are Pass"
print("*************************************")
print("\tSOMAIYA UNIVERSITY")
for x in score:
    status = "fail"
    if x >= 35:
        status = "pass"
    else:
        s = "You are Fail"
    print("Subject :", x , status)
print("********",s,"*****")
print("*************************************")
