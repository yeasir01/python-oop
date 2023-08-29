from school import School, Teacher, Course, Student

# School
uc_davis = School("UC Davis", "USA")

# Teachers
teacher_1 = Teacher("Dean", "Sirianni")
teacher_2 = Teacher("Marvin", "Haskamp")
teacher_3 = Teacher("Justin", "Gribble")

# Courses
python_course = Course("Intro to Python", teacher_1, 50)
javascript_course = Course("Intro to Javascript", teacher_2, 75)
cpp_course = Course("Intro to Programming with C++", teacher_3, 100)

# Students
student_1 = Student("Jake", "Wilson", 123, "12/29/1986")
student_2 = Student("Mike", "Hughes", 124, "12/29/1977")
student_3 = Student("Jeff", "Kelly", 125, "01/29/1980")

# Methods
uc_davis.add_courses([python_course, javascript_course, cpp_course])
uc_davis.enroll_students([student_1, student_2, student_3])

student_1.enroll_course(javascript_course)
student_1.enroll_course(cpp_course)

student_2.enroll_course(javascript_course)

student_3.enroll_course(python_course)
student_3.enroll_course(cpp_course)

# Visualize your data [🤩]
print("Teachers: ", uc_davis.teachers)
print("Courses: ", uc_davis.courses)
print("Students: ", uc_davis.students)
print("Mikes Age (student): ", student_2.age)
print("Jake Wilson Courses: ", student_1.course_list)

""" 
Console Output

Teachers:  [Dean Sirianni, Marvin Haskamp, Justin Gribble]
Courses:  [Intro to Python, Intro to Javascript, Intro to Programming with C++]
Students:  [Jake Wilson, Mike Hughes, Jeff Kelly]
Mikes Age (student):  45
Jake Wilson Courses:  [Intro to Javascript, Intro to Programming with C++]
"""