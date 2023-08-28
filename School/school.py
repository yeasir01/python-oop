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

    def add_courses(self, courses: list):
        for course in courses:
            if not isinstance(course, Course):
                raise TypeError("Must be a type of course.")
            else:
                self.courses.append(course)

    @property
    def teachers(self):
        teachers = set()
        for course in self.courses:
            teachers.add(course.teacher)
        return teachers


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
    pass
