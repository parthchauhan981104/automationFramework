from pages.courses.register_courses_pages import RegisterCoursesPage
from pages.home.navigation_page import NavigationPage
from utilities.test_status import TestStatus
import unittest, pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
import time

#export PYTHONPATH=$(pwd)
#or
#export PYTHONPATH=$PYTHONPATH
#py.test -s -v tests/home/register_courses_csv_data.py --browser chrome

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.nav.navigateToAllCourses()

    @pytest.mark.run(order=1)
    @data(*getCSVData("/Users/Parth\PycharmProjects/automationFramework/tests/courses/testdata.csv"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVV):
        self.courses.enterCourseName(courseName)
        time.sleep(1)
        self.courses.selectCourseToEnroll(courseName)
        time.sleep(1)
        self.courses.enrollCourse(num=ccNum, exp=ccExp, cvv=ccCVV)
        time.sleep(1)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result,
                          "Enrollment Failed Verification")