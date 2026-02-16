Employee = (
           (101,"A","IT"),
           (102,"B","LeaderShip"),
           (103,"C","Infrastructure"),
           (104,"D","HR"),
           (105,"E","Security"),
           (106,"F","Admin"),
           (107,"G","Payroll") )

roles = {"admin", "editor", "viewer"}


for individualEmp in Employee:
    print("ID:", individualEmp[0])
    print("Name:", individualEmp[1])
    print("Department:", individualEmp[2])
    print("----")  # separator for clarity

print("Printing with Tuple index")
print("**" *50)
print("Name:", Employee[0][1],"||","ID:",Employee[0][0],"||","Department:",Employee[0][2])
print("Name:", Employee[1][1],"||","ID:",Employee[1][0],"||","Department:",Employee[1][2])
print("Name:", Employee[2][1],"||","ID:",Employee[2][0],"||","Department:",Employee[2][2])
print("Name:", Employee[3][1],"||","ID:",Employee[3][0],"||","Department:",Employee[3][2])
print("Name:", Employee[4][1],"||","ID:",Employee[4][0],"||","Department:",Employee[4][2])
print("Name:", Employee[5][1],"||","ID:",Employee[5][0],"||","Department:",Employee[5][2])
print("Name:", Employee[6][1],"||","ID:",Employee[6][0],"||","Department:",Employee[6][2])

print("Printing with Tuple index via loop")
print("**" *50)
for i in range(len(Employee)):
    print("Name:", Employee[i][1],"##","ID:",Employee[i][0],"##","Department:",Employee[i][2])


if "admin" in roles:
    print("Admin Access: Yes")
else:
    print("Admin Access: No")
