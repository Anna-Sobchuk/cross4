import os
import unittest
from collections import defaultdict
from main import handle_create, handle_add, handle_subtract, handle_increment, handle_print, variables


class TestVirtualMachine(unittest.TestCase):
    def setUp(self):
        self.variables = defaultdict(int)

    def test_variable_creation(self):
        command_content = ['Create', 'c', '6']
        command_content2 = ['Create', 'e', '245']
        handle_create(command_content)
        handle_create(command_content2)
        self.assertEqual(variables['c'], 6)
        self.assertEqual(variables['e'], 245)

    def test_add_variables(self):
        variables['c'] = 6
        variables['e'] = 245

        command_content = ['Add', 'c', 'e']
        handle_add(command_content)
        self.assertEqual(variables['c'], 251)

    def test_add_variable_and_number(self):
        variables['e'] = 245

        command_content = ['Add', 'e', '78']
        handle_add(command_content)
        self.assertEqual(variables['e'], 323)

    def test_subtract_variables(self):
        variables['e'] = 245
        variables['c'] = 6

        command_content = ['Subtract', 'e', 'c']
        handle_subtract(command_content)
        self.assertEqual(variables['e'], 239)

    def test_subtract_variable_and_number(self):
        variables['c'] = 200

        command_content = ['Subtract', 'c', '200']
        handle_subtract(command_content)
        self.assertEqual(variables['c'], 0)

    def test_increment_variable(self):
        variables['c'] = 51

        command_content = ['Increment', 'c']
        handle_increment(command_content)
        self.assertEqual(variables['c'], 52)

if __name__ == '__main__':
    unittest.main()