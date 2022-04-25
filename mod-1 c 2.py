import statistics
marks_sheet=dict()
for i in range(int(input("Enter number off students:"))):
    print("student-",i+1)
    name=input("Enter name:")
    marks=[int(i) for i in input().split()]
    marks_sheet[name]=marks
name_=input("Enter name:")
if name_ in marks_sheet:
    print(round(statistics.mean(marks_sheet[name_]),2))
else:
    print("Not recorded..")