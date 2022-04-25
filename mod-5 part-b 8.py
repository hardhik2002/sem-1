class students:
    def __init__(self):
        self.name=[i for i in input("Enter name:").split()]
        self.marks=[[int(input()) for i in range(0,3)] for j in range(len(self.name))]
    def display(self):
        self.student_marks=zip(self.name,self.marks)
        for name,marks in self.student_marks:
            print(name,marks)
std=students()
std.display()