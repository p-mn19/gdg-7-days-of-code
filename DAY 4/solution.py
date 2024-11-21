x=int(input("Enter number of colleges: "))
y=int(input("Enter number of students: "))
z=int(input("Enter number of students who passed: "))
percent=100*(z/(x*y))
if(percent>50):
    print("YES")
else:
  print("NO")
