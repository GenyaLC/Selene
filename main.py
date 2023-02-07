import sys, json
from inspector import open_files, detect_functions, scan_functions
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Help: python", sys.argv[0], "path")
        sys.exit()
    
    files = open_files(sys.argv[1])
    functions = []
    
    for name, content in files.items():
        functions = functions + scan_functions(content)
    print()
    print()
    print()
    print(functions)
    print()
    for name, content in files.items():
        print(name)
        raw = detect_functions(content, functions)
        json_object = json.dumps(raw, indent=4)
        print(json_object)
        