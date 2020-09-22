from pages.courses.register_courses_pages import RegisterCoursesPage
from utilities.test_status import TestStatus
import unittest
import pytest

#export PYTHONPATH=$(pwd)
#or
#export PYTHONPATH=$PYTHONPATH
#py.test -s -v tests/home/register_courses_tests.py --browser chrome

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        self.courses.enterCourseName("JavaScript")
        self.courses.selectCourseToEnroll("JavaScript for beginners")
        self.courses.enrollCourse(num="1234 5678 9012 3456", exp="1220", cvv="444", zip="12345")
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result,
                          "Enrollment Failed Verification")