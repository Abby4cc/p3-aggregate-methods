from datetime import datetime

class Student:
    def __init__(self, name):
        self.name = name
        self._enrollments = []

    def enroll(self, course):
        if isinstance(course, Course):
            enrollment = Enrollment(self, course)
            self._enrollments.append(enrollment)
            course.add_enrollment(enrollment)
        else:
            raise TypeError("course must be an instance of Course")

    def get_enrollments(self):
        return self._enrollments.copy()

    def course_count(self):
        """Return the number of courses the student is enrolled in."""
        return len(self._enrollments)

    def aggregate_average_enrollment_time(self):
        """Return the average number of days since enrollment across all courses."""
        if not self._enrollments:
            return 0
        total_days = 0
        now = datetime.now()
        for enrollment in self._enrollments:
            delta = now - enrollment.get_enrollment_date()
            total_days += delta.days
        return total_days / len(self._enrollments)


class Course:
    def __init__(self, title):
        self.title = title
        self._enrollments = []

    def add_enrollment(self, enrollment):
        if isinstance(enrollment, Enrollment):
            self._enrollments.append(enrollment)
        else:
            raise TypeError("enrollment must be an instance of Enrollment")

    def get_enrollments(self):
        return self._enrollments.copy()


class Enrollment:
    all = []
    
    def __init__(self, student, course):
        if isinstance(student, Student) and isinstance(course, Course):
            self.student = student
            self.course = course
            self._enrollment_date = datetime.now()
            type(self).all.append(self)
        else:
            raise TypeError("Invalid types for student and/or course")

    def get_enrollment_date(self):
        return self._enrollment_date

    @classmethod
    def aggregate_enrollments_per_day(cls):
        """Return a dict with enrollment date (date only) as keys and count of enrollments on that date as values."""
        enrollment_count = {}
        for enrollment in cls.all:
            date_key = enrollment.get_enrollment_date().date()
            enrollment_count[date_key] = enrollment_count.get(date_key, 0) + 1
        return enrollment_count
