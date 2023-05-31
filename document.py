import os
import pydoc

def generate_documentation(directory):
    files = get_python_files(directory)
    for file in files:
        module_name = get_module_name(file)
        output_path = get_output_path(file)
        with open(output_path, 'w') as f:
            pydoc.doc(module_name, output=f)

def get_python_files(directory):
    python_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    return python_files

def get_module_name(file):
    return os.path.splitext(os.path.basename(file))[0]

def get_output_path(file):
    directory = os.path.dirname(file)
    module_name = get_module_name(file)
    output_path = os.path.join(directory, module_name + '.html')
    return output_path

# Example usage
directory = '/home/sp4rk/IdeaProjects/kriya'
generate_documentation(directory)
