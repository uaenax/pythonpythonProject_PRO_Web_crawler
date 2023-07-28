class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.grades = {"语文":0, "数学":0,"英语":0}

    def set_grades(self, course,grade):
        if course in self.grades:
            self.grades[course] = grade

        # return self.grades
    def print_grades(self):
        print(f"学生:{self.name} (学号:{self.id})\n"f"成绩:{self.grades}")
        for course in self.grades:
            print(f"{course}:{self.grades[course]}分")
        # return self.grades
a = Student("张三","01")
a.set_grades("语文",90)
a.print_grades()