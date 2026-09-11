#Accept marks of 6 students and display them sorted
marks=[]
for i in range(6):
    mark=int(input("enter marks: "))
    marks.append(mark)
marks.sort()
print(marks)