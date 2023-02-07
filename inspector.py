import os

#TODO: os.walk improves this
def get_filepath(dir:str) -> list:
    '''Gets every python file on directory recursively'''
    content = os.listdir(dir)
    python_files = []
    for file in content:
        if os.path.isfile(os.path.join(dir, file)) and file.endswith('.py'):
            python_files.append(os.path.join(dir, file))
        if os.path.isdir(os.path.join(dir,file)):
            for subfile in get_filepath(os.path.join(dir,file)):
                python_files.append(os.path.join(file, subfile))
    return python_files


def open_files(dir:str) -> dict:
    '''Makes a dict with filename:content'''
    dict_file = {}
    for file in get_filepath(dir):
       f = open(file, 'r')
       dict_file[file] = f.read()
    return dict_file


def scan_functions(input:str) -> list:
    '''Search funcions'''
    functions = []
    parsed = input.split('\n')
    for line in parsed:
        if line.find('def ') % 2 == 0 or line.find(' def ') != -1:
            functions.append(line.split(':\n')[0])
    return functions


def detect_functions(input:str, functions:list) -> dict:
    '''Detect the usage of functions'''
    parsed_input = input.split('\n\n')
    function_name = [x.split('def ')[1].split('(')[0] for x in functions]
    actual = 'variable declaration'
    contained = []
    result = {}
    for i in parsed_input:
        for name in function_name:
            if i.find(name+'(') == 0:
                actual = name
            elif actual == 'variable declaration':
                continue
                # contained.append([name, i.split(name)[1].split(')')[0]])
            elif i.find(name+'(') != -1:
                contained.append([name, i.split(name)[1].split(')')[0] + ')'])
        result[actual] = contained
        contained = []
        actual = ''
    return result
                
def find_classes(input:str):
    pass


def sum_relations():
    pass