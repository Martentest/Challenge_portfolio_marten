import unittest

from unittest.loader import makeSuite

from test_cases.login_to_the_system import TestLogin
from test_cases.login_check_title import TestLoginTitle
from test_cases.dashboard_check_title import TestDashboardTitle
from test_cases.add_a_player_test import TestAddPlayer
from test_cases.add_a_player_check_title import TestAddPlayerTitle

def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(TestLogin))
   test_suite.addTest(makeSuite(TestLoginTitle))
   test_suite.addTest(makeSuite(TestDashboardTitle))
   test_suite.addTest(makeSuite(TestAddPlayer))
   test_suite.addTest(makeSuite(TestAddPlayerTitle))
   return test_suite

if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())