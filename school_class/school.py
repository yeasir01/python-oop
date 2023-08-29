from datetime import date

class School:
    def __init__(self, name: str, country: str):
        self.name = name
        self.courses = []
        self.students = []
        self.country = country

    def add_course(self, course: object):
        if not isinstance(course, Course):
            raise TypeError("Must be a type of course.")
        else:
            self.courses.append(course)

    def add_courses(self, courses: list[object]):
        for course in courses:
            if not isinstance(course, Course):
                raise TypeError("Must be a type of course.")
            else:
                self.courses.append(course)
    
    def enroll_student(self, student: object):
        if not isinstance(student, Student):
            raise TypeError("Must be a type of student.")
        else:
            self.students.append(student)
    
    def enroll_students(self, students: list[object]):
        for student in students:
            if not isinstance(student, Student):
                raise TypeError("Must be a type of student.")
            else:
                self.students.append(student)

    @property
    def teachers(self):
        teachers = set()
        for course in self.courses:
            teachers.add(course.teacher)
        return list(teachers)


class Course:
    def __init__(self, name: str, teacher: object, credits: int):
        """
        Parameters
            @name: name of course.
            @teacher: instance of teacher class
            @credit: pass a credit value.

        Raise
            TypeError: is raised if a teacher instance is not passed.
        """
        self.name = name
        if not isinstance(teacher, Teacher):
            raise TypeError("Must be a type of teacher.")
        self.teacher = teacher
        self.credits = credits

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"


class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"


class Teacher(Person):
    pass


class Student(Person):
    def __init__(self, first_name: str, last_name: str, student_id: str, birth_date: str):
        super().__init__(first_name, last_name)
        self.course_list = []
        self.student_id = student_id
        self.birth_date = birth_date
    
    @property
    def age(self):
        today = date.today()
        date_list = self.birth_date.split("/")
        born = date(int(date_list[2]), int(date_list[0]), int(date_list[1]))
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    
    def enroll_course(self, course: object):
        if not isinstance(course, Course):
            raise TypeError("Must be a type of course.")
        else:
            self.course_list.append(course)

    @property
    def courses(self):
        return self.courses