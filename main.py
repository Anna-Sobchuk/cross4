import os
from collections import defaultdict

variables = defaultdict(int)

def handle_create(command_content):
    variable_name = command_content[1]
    variable_value = int(command_content[2])
    variables[variable_name] = variable_value


def handle_add(command_content):
    if not command_content[1] or not command_content[2]:
        raise ValueError("No variables to add")

    var1 = variables.get(command_content[1], 0)

    if command_content[2].isdigit():
        var2 = int(command_content[2])
    else:
        var2 = variables.get(command_content[2], 0)

    variables[command_content[1]] = var1 + var2


def handle_subtract(command_content):
    if not command_content[1] or not command_content[2]:
        raise ValueError("No variables to subtract")

    var1 = variables.get(command_content[1], 0)

    if command_content[2] in variables:
        var2 = variables[command_content[2]]
    elif command_content[2].isdigit():
        var2 = int(command_content[2])
    else:
        raise ValueError(f"Variable {command_content[2]} does not exist")

    variables[command_content[1]] = var1 - var2


def handle_increment(command_content):
    if not command_content[1]:
        raise ValueError("No variable to increment")

    variables[command_content[1]] = variables.get(command_content[1], 0) + 1


def handle_print(command_content):
    if not command_content[1]:
        raise ValueError("No variable to print")

    variable = variables.get(command_content[1])
    if variable is None:
        raise ValueError("No value to print")
    else:
        print(variable)


file_path = os.path.join(os.path.dirname(__file__), 'test_virtual_machine')
file_content = []

with open(file_path, 'r', encoding='utf-8') as file:
    file_content = [line.strip() for line in file if line.strip()]

i = 0
while i < len(file_content):
    command_clean = file_content[i].replace(",", "")
    command_content = command_clean.split(" ")

    if command_content[0] == 'Create':
        handle_create(command_content)
    elif command_content[0] == 'Add':
        handle_add(command_content)
    elif command_content[0] == 'Subtract':
        handle_subtract(command_content)
    elif command_content[0] == 'Increment':
        handle_increment(command_content)
    elif command_content[0] == 'Print':
        handle_print(command_content)
    i += 1

