with open("students.txt", "w") as f:
    f.write("101, Alice, 85\n102, Bob, 78\n103, Charlie, 92\n104, Diana, 66\n105, Evan, 49")

class Student:
    def __init__(self, id, name, marks):
        self.id = id
        self.name = name
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif 80 <= self.marks < 90:
            return "B"
        elif 70 <= self.marks < 80:
            return "C"
        elif 60 <= self.marks < 70:
            return "D"
        else:
            return "F"

grade_stat = {}
print("Students Report:")
try:
    with open("students.txt", "r") as file, open("grade.txt", "w") as new:
        for line in file:
            words = line.strip().split(', ')
            id = int(words[0])
            name = words[1]
            marks = int(words[2])
            student = Student(id, name, marks)
            grade = student.get_grade()
            print(f"ID: {id:<3} | Name: {name:<8} | Grade: {grade}")
            if grade in grade_stat:
                grade_stat[grade] += 1
            else:
                grade_stat[grade] = 1
            new.write(f"ID: {id:<3} | Name: {name:<8} | Grade: {grade}\n")

except FileNotFoundError as e:
    print("ExceptionOccurred: File not found!")

print("\nGrade Summary:")
for g in sorted(grade_stat):
    print(f"Grade {g}: {grade_stat[g]} student(s)")



