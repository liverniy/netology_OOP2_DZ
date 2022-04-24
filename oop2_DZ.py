class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lectors(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached \
                and (course in self.finished_courses or course in self.courses_in_progress):
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        all_grades = []

        for course in self.grades:
            all_grades.extend(self.grades[course])
        if len(all_grades) > 0:
            avg_grade = round(sum(all_grades) / len(all_grades), 1)
        else:
            avg_grade = 0

        courses_in_progress_str = ", ".join(self.courses_in_progress)
        finished_courses_str = ", ".join(self.finished_courses)

        some_student = f"""
Имя:{self.name}
Фамилия:{self.surname}
Средняя оценка за домашние задание:{avg_grade}
Курсы в процессе изучения:{courses_in_progress_str}
Завершенные курсы:{finished_courses_str}
"""
        return some_student

    def __lt__(self, other):
        if isinstance(other, Student):
            self_grades = []
            other_grades = []

            for course in self.grades:
                self_grades.extend(self.grades[course])
            for course in other.grades:
                other_grades.extend(other.grades[course])
            if len(self_grades) > 0:
                self_avg_grade = sum(self_grades) / len(self_grades)
            else:
                self_avg_grade = 0
            if len(other_grades) > 0:
                other_avg_grade = sum(other_grades) / len(other_grades)
            else:
                other_avg_grade = 0

            return self_avg_grade < other_avg_grade


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
        all_grades = []
        for course in self.grades:
            all_grades.extend(self.grades[course])
        if len(all_grades) > 0:
            avg_grade = round(sum(all_grades) / len(all_grades), 1)
        else:
            avg_grade = 0
        some_lecturer = f"Имя:{self.name}\nФамилия:{self.surname}\n"
        some_lecturer += f"Средняя оценка за лекции:{avg_grade}"
        return some_lecturer

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            self_grades = []
            other_grades = []
            for course in self.grades:
                self_grades.extend(self.grades[course])
            for course in other.grades:
                other_grades.extend(other.grades[course])
            if len(self_grades) > 0:
                self_avg_grade = sum(self_grades) / len(self_grades)
            else:
                self_avg_grade = 0

            if len(other_grades) > 0:
                other_avg_grade = sum(other_grades) / len(other_grades)
            else:
                other_avg_grade = 0

            return self_avg_grade < other_avg_grade


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        some_reviewer = f"Имя:{self.name}\nФамилия:{self.surname}\n"
        return some_reviewer


def student_avg_course_grade(students, course):
    all_grades = []

    for student in students:
        if course in student.grades:
            all_grades.extend(student.grades[course])

    if len(all_grades) > 0:
        avg_grade = round(sum(all_grades) / len(all_grades), 1)
    else:
        return f"За курс {course} студенты ещё не получали оценок."

    return f"Средняя оценка студентов за курс {course}: {avg_grade}"


def lecturer_avg_course_grade(lecturers, course):
    all_grades = []

    for lecturer in lecturers:
        if course in lecturer.grades:
            all_grades.extend(lecturer.grades[course])

    if len(all_grades) > 0:
        avg_grade = round(sum(all_grades) / len(all_grades), 1)
    else:
        return f"За курс {course} лекторы ещё не получали оценок."

    return f"Средняя оценка лекторов за курс {course}: {avg_grade}"


def main():
    student1 = Student("Иван", "Иванов", "муж")
    student2 = Student("Светлана", "Петрова", "жен")
    reviewer1 = Reviewer("Николай", "Николаев")
    reviewer2 = Reviewer("Галина", "Малинина")
    lecturer1 = Lecturer("Иосиф", "Кобзон")
    lecturer2 = Lecturer("Марк", "Бернес")

    student1.finished_courses += ["Java"]
    student1.courses_in_progress += ["Python", "SQL", "C++"]

    student2.finished_courses += ["Java"]
    student2.courses_in_progress += ["Python", "C++"]

    lecturer1.courses_attached += ["Java", "Python", "C++", "SQL"]
    lecturer2.courses_attached += ["SQL", "C++"]

    reviewer1.courses_attached += ["Java", "Python", "C++", "SQL"]
    reviewer2.courses_attached += ["Java", "Python", "SQL", "C++"]

    student1.rate_lectors(lecturer1, "Java", 5)
    student1.rate_lectors(lecturer1, "Python", 4)
    student1.rate_lectors(lecturer1, "C++", 10)
    student1.rate_lectors(lecturer1, "SQL", 7)
    student1.rate_lectors(lecturer2, "C++", 10)
    student1.rate_lectors(lecturer2, "SQL", 6)

    student2.rate_lectors(lecturer1, "Java", 8)
    student2.rate_lectors(lecturer1, "Python", 2)
    student2.rate_lectors(lecturer1, "C++", 10)
    student2.rate_lectors(lecturer2, "C++", 9)

    reviewer1.rate_hw(student1, "Python", 4)
    reviewer1.rate_hw(student1, "C++", 3)
    reviewer1.rate_hw(student1, "SQL", 8)
    reviewer1.rate_hw(student2, "Python", 7)
    reviewer1.rate_hw(student2, "C++", 9)

    reviewer2.rate_hw(student1, "Python", 10)
    reviewer2.rate_hw(student1, "C++", 2)
    reviewer2.rate_hw(student1, "SQL", 10)
    reviewer2.rate_hw(student1, "Java", 4)

    reviewer2.rate_hw(student2, "Python", 4)
    reviewer2.rate_hw(student2, "C++", 3)
    reviewer2.rate_hw(student2, "Java", 3)

    print(f"Студенты: \n{student1}\n{student2}")
    print(f"Лекторы: \n{lecturer1}\n{lecturer2}")
    print(f"Проверяющие: \n{reviewer1}\n{reviewer2}")

    if lecturer1 > lecturer2:
        print(f"Средняя оценка у {lecturer1.name} {lecturer1.surname} выше чем {lecturer2.name} {lecturer2.surname}.")
    elif lecturer1 == lecturer2:
        print(f"Средняя оценка у лекторов {lecturer1.surname} и {lecturer2.surname} равна.")
    else:
        print(f"Средняя оценка у {lecturer2.name} {lecturer2.surname} выше чем {lecturer1.name} {lecturer1.surname}.")

    if student1 > student2:
        print(f"Средняя оценка у {student1.name} {student1.surname} выше чем {student2.name} {student2.surname}.")
    elif student1 == student2:
        print(f"Средняя оценка у студентов {student1.surname} и {student2.surname} равна.")
    else:
        print(f"Средняя оценка у {student2.name} {student2.surname} выше чем {student1.name} {student1.surname}.")

    students = [student1, student2]
    lecturers = [lecturer1, lecturer2]
    courses = ["Python", "Java", "C++", "SQL"]

    for course in courses:
        print(lecturer_avg_course_grade(lecturers, course))
        print(student_avg_course_grade(students, course), "\n")


main()
