import re


class Student:
    """ Student Class - Maintains the details of a student """

    FIRST_NAME_LABEL = "First Name"
    LAST_NAME_LABEL = "Last Name"
    STUDENT_NUM_LABEL = "Student Number"
    PROGRAM_LABEL = "Program"
    COURSE_ID_LABEL = "Course ID"

    STUDENT_NUM_RE = "[A-Z][0-9]{10}"

    def __init__(self, first_name, last_name, student_number, program):
        """ Constructor - Initializes the main attributes of a student """

        Student._validate_string_input(Student.FIRST_NAME_LABEL, first_name)
        self._first_name = first_name

        Student._validate_string_input(Student.LAST_NAME_LABEL, last_name)
        self._last_name = last_name

        Student._validate_string_input(Student.STUDENT_NUM_LABEL, student_number)

        if re.match(Student.STUDENT_NUM_RE, student_number) is None:
            raise ValueError("Student number is invalid")

        self._student_number = student_number

        Student._validate_string_input(Student.PROGRAM_LABEL, program)
        self._program = program

        self._courses = []

    def get_student_number(self):
        """ Returns the student number """
        return self._student_number

    def get_program(self):
        """ Returns the program the student is enrolled in """
        return self._program

    def add_course(self, course_id):
        """ Adds a course to the student. Rejects duplicate courses. """
        Student._validate_string_input(Student.COURSE_ID_LABEL, course_id)

        if not self.is_enrolled_in_course(course_id):
            self._courses.append(course_id)

    def remove_course(self, course_id):
        """ Removes a course from a student """

        Student._validate_string_input(Student.COURSE_ID_LABEL, course_id)

        if self.is_enrolled_in_course(course_id):
            self._courses.remove(course_id)

    def is_enrolled_in_course(self, course_id):
        """ Checks if enrolled in course """

        Student._validate_string_input(Student.COURSE_ID_LABEL, course_id)

        if self._courses.count(course_id) > 0:
            return True

        return False

    def get_num_courses(self):
        """ Returns the number of courses a student is enrolled in """
        return len(self._courses)

    def get_details(self):
        """ Returns the student details in a printable format """
        course_list = "None"

        if len(self._courses) > 0:
            course_list = ', '.join(str(x) for x in self._courses)

        details = self._first_name + " " + self._last_name + " is a student in the " + self._program + \
                  " Program taking the following courses: " + course_list

        return details

    @classmethod
    def _validate_string_input(cls, display_name, str_value):
        """ Private helper to validate string values """

        if str_value is None:
            raise ValueError(display_name + " cannot be undefined.")

        if str_value == "":
            raise ValueError(display_name + " cannot be empty.")
