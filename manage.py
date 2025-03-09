class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)
        print(f"{self.name} enrolled in {course}")

    def show_courses(self):
        return f"{self.name} is enrolled in: {', '.join(self.courses)}"

class Teacher:
    def __init__(self, teacher_id, name, subject):
        self.teacher_id = teacher_id
        self.name = name
        self.subject = subject
        self.students = {}

    def assign_grade(self, student, course, grade):
        if course in student.courses:
            self.students[student.name] = {course: grade}
            print(f"{self.name} assigned grade {grade} to {student.name} for {course}")
        else:
            print(f"{student.name} is not enrolled in {course}")

    def show_students(self):
        return self.students

class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} added to {self.name}")

    def add_teacher(self, teacher):
        self.teachers.append(teacher)
        print(f"Teacher {teacher.name} added to {self.name}")

    def list_students(self):
        return [student.name for student in self.students]

    def list_teachers(self):
        return [teacher.name for teacher in self.teachers]

school = School("Greenwood High")

student1 = Student(1, "Alice", "10th")
teacher1 = Teacher(101, "Mr. Smith", "Mathematics")

school.add_student(student1)
school.add_teacher(teacher1)

student1.enroll("Mathematics")

teacher1.assign_grade(student1, "Mathematics", "A")

print(student1.show_courses())
print(teacher1.show_students())
