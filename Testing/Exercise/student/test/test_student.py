from unittest import TestCase, main

from project_student_testing.student import Student


class StudentTest(TestCase):

    def test_init_method_working_properly_with_courses_passed(self):
        student = Student("Kumanov", {"Math": ["Algebra", "Geometry"]})
        self.assertEqual("Kumanov", student.name)
        self.assertEqual({"Math": ["Algebra", "Geometry"]}, student.courses)

    def test_init_method_working_properly_with_no_courses_passed(self):
        student = Student("Kumanov")
        self.assertEqual({}, student.courses)
        self.assertEqual("Kumanov", student.name)

    def test_enroll_new_course_and_adds_notes_if_empty_str_or_Y_is_passed_as_comment(self):
        student = Student("Kumanov")
        expected = "Course and course notes have been added."
        self.assertEqual(expected, student.enroll("Computer Science", ["Note2"], "Y"))
        self.assertEqual(1, len(student.courses))
        self.assertEqual(1, len(student.courses["Computer Science"]))
        result = student.enroll("Math", ["Note2"], "")
        self.assertEqual(expected, result)
        self.assertEqual(2, len(student.courses))
        self.assertEqual(1, len(student.courses["Math"]))
        expected = {"Computer Science": ["Note2"], "Math": ["Note2"]}
        self.assertEqual(expected, student.courses)

    def test_enroll_checks_appends_notes_to_existing_course_and_returns_msg(self):
        student = Student("Kumanov", {'Computer Science': ['Note1']})
        expected = "Course already added. Notes have been updated."
        result = student.enroll("Computer Science", ["Note2"])
        self.assertEqual(expected, result)
        expected_dict = {"Computer Science": ["Note1", "Note2"]}
        self.assertEqual(2, len(student.courses["Computer Science"]))
        self.assertEqual(expected_dict, student.courses)

    def test_enroll_new_course_and_add_notes_if_other_than_y_or_empty_is_passed_as_comment(self):
        student = Student("Kumanov")
        expected = "Course has been added."
        self.assertEqual(expected, student.enroll("Math", ["Note1"], "n"))
        self.assertEqual(1, len(student.courses))
        self.assertEqual(0, len(student.courses["Math"]))

    def test_enroll_new_course_and_doesnt_pass_notes(self):
        student = Student("Kumanov")
        expected = "Course has been added."
        self.assertEqual(expected, student.enroll("Math", ["Note1"], "n"))
        self.assertEqual(0, len(student.courses["Math"]))

    def test_add_notes_to_existing_course(self):
        student = Student("Kumanov", {"Math": ["Note1"]})
        expected = "Notes have been updated"
        self.assertEqual(expected, student.add_notes("Math", "Note2"))

    def test_add_notes_to_existing_course_with_no_notes(self):
        student = Student("Kumanov", {"Math": []})
        expected = "Notes have been updated"
        self.assertEqual(expected, student.add_notes("Math", "Note2"))

    def test_add_notes_no_course_found_raise(self):
        student = Student("Kumanov", {"Math": []})
        expected = "Cannot add notes. Course not found."
        with self.assertRaises(Exception) as ex:
            student.add_notes("Biology", "Note1")
        self.assertEqual(expected, str(ex.exception))

    def test_leave_course_checks_if_course_is_in_and_pops_it(self):
        student = Student('Alexander', {"Math": []})
        expected = "Course has been removed"
        expected_len = 0
        self.assertEqual(expected, student.leave_course("Math"))
        self.assertEqual(expected_len, len(student.courses))
        self.assertEqual({}, student.courses)

    def test_leave_course_course_not_found_raises_exc(self):
        student = Student("Alexander", {"Math": []})
        expected = "Cannot remove course. Course not found."
        with self.assertRaises(Exception) as ex:
            student.leave_course("Computer Science")
        self.assertEqual(expected, str(ex.exception))


if __name__ == '__main__':
    main()
