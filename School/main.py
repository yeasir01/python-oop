from school import School, Teacher, Course, Student

#School
uc_davis = School("UC Davis", "USA")

#Teachers
teacher_1 = Teacher("Dean", "Sirianni")
teacher_2 = Teacher("Marvin", "Haskamp")
teacher_3 = Teacher("Justin", "Gribble")

#Courses
python_course = Course("Intro to Python", teacher_1, 50)
javascript_course = Course("Intro to Javascript", teacher_2, 75)
cpp_course = Course("Intro to Programming with C++", teacher_3, 100)

#Students
student_1 = Student("Jake", "Wilson")
student_2 = Student("Mike", "Hughes")
student_3 = Student("Jeff", "Kelly")

#Methods
uc_davis.add_courses([python_course, javascript_course, cpp_course])

print(uc_davis.teachers)