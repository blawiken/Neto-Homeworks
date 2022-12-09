class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        res = f'Имя: {self.name} \
        \nФамилия: {self.surname} \
        \nСредняя оценка за домашние задания: {self.average_grade()} \
        \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \
        \nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other_student):
        if isinstance(other_student, Student):
            return self.average_grade() < other_student.average_grade()

    def rate_hw(self, lecturer, course, grade):
        if (
            isinstance(lecturer, Lecturer)
            and course in self.courses_in_progress
            and course in lecturer.courses_attached
        ):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        if len(self.grades) == 0:
            return 0
        sum_grade = 0.0
        for grades_list in self.grades.values():
            for count, grade in enumerate(grades_list):
                sum_grade += grade
        return sum_grade / (count + 1)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        res = f'Имя: {self.name} \
        \nФамилия: {self.surname} \
        \nСредняя оценка по лекции: {self.average_grade()}'
        return res

    def __lt__(self, other_lecturer):
        if isinstance(other_lecturer, Lecturer):
            return self.average_grade() < other_lecturer.average_grade()

    def average_grade(self):
        if len(self.grades) == 0:
            return 0
        sum_grade = 0.0
        for grades_list in self.grades.values():
            for count, grade in enumerate(grades_list):
                sum_grade += grade
        return sum_grade / (count + 1)

class Reviewer(Mentor):
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if (
            isinstance(student, Student)
            and course in self.courses_attached
            and course in student.courses_in_progress
        ):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def average_grades_for_students(students, course):
    '''
    Подсчёт средней оценки за домашние задания по всем студунам в рамках конкретного курса.
    '''
    grades_current_student = 0.0
    averge_grades_all_students = 0.0
    for student in students:
        if course in student.grades:
            for count, grade in enumerate(student.grades[course]):
                grades_current_student += grade
            averge_grades_all_students += grades_current_student / (count + 1)
            grades_current_student = 0.0
    res = f'Средняя оценка за домашние задания: {round(averge_grades_all_students / len(students), 1)}\
            \nКурс: {course}, кол-во студентов: {len(students)}'
    return res


def average_grades_for_lecturers(lecturers, course):
    '''
    Подсчёт средней оценки за домашние задания для всех лекторов в рамках конкретного курса.
    '''
    grades_current = 0.0
    averge_grades = 0.0
    for lecturer in lecturers:
        if course in lecturer.grades:
            for count, grade in enumerate(lecturer.grades[course]):
                grades_current += grade
            averge_grades += grades_current / (count + 1)
            grades_current = 0.0
    res = f'Средняя оценка за лекции: {round(averge_grades / len(lecturers), 1)}\
            \nКурс: {course}, кол-во лекторов: {len(lecturers)}'
    return res


student_1 = Student('Joseph', 'Evans', 'Male')
student_2 = Student('Olivia', 'Smith', 'Female')
lecturer_1 = Lecturer('Thomas', 'Davies')
lecturer_2 = Lecturer('Amelia', 'Brown')
reviewer_1 = Reviewer('Jack', 'Aldridge')
reviewer_2 = Reviewer('Jessica', 'Harris')

student_1.courses_in_progress.append('Python')
student_1.courses_in_progress.append('Git')
student_1.finished_courses.append('Adobe Photoshop')
reviewer_1.courses_attached.append('Python')
reviewer_2.courses_attached.append('Git')
reviewer_1.rate_hw(student_1, 'Python', 3.4)
reviewer_1.rate_hw(student_1, 'Python', 6.8)
reviewer_2.rate_hw(student_1, 'Git', 1.2)
print(student_1)

lecturer_1.courses_attached.append('Git')
student_1.rate_hw(lecturer_1, 'Git', 4.5)
student_1.rate_hw(lecturer_1, 'Git', 7.2)
print(lecturer_1)
print(reviewer_1)

print(student_2)
print(lecturer_2)

student_2.courses_in_progress.append('Python')
reviewer_1.rate_hw(student_2, 'Python', 9.9)
print(student_1 > student_2)
print(lecturer_1 > lecturer_2)

students_list = [student_1, student_2]
print(average_grades_for_students(students_list, 'Python'))
print(average_grades_for_students(students_list, 'Git'))

lecturer_list = [lecturer_1, lecturer_2]
print(average_grades_for_lecturers(lecturer_list, 'Python'))
print(average_grades_for_lecturers(lecturer_list, 'Git'))