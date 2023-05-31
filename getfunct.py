import os
import inspect

def get_methods_and_functions(directory):
    methods_and_functions = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    code = f.read()
                    module = compile(code, file_path, "exec")
                    functions = inspect.getmembers(module, inspect.isfunction)
                    methods = inspect.getmembers(module, inspect.ismethod)
                    methods_and_functions.extend(functions + methods)
    return methods_and_functions

def write_methods_and_functions_to_file(methods_and_functions, output_file):
    with open(output_file, "w") as f:
        for name, _ in methods_and_functions:
            f.write(name + "\n")

# Example usage
directory = "/home/sp4rk/IdeaProjects/kriya"
output_file = "methods_and_functions.txt"

methods_and_functions = get_methods_and_functions(directory)
write_methods_and_functions_to_file(methods_and_functions, output_file)
