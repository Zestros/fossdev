import ast
import os
import sys

def get_imports(directory):
    imports = set()
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                    tree = ast.parse(f.read())
                    for node in ast.walk(tree):
                        if isinstance(node, ast.Import):
                            for n in node.names:
                                imports.add(n.name.split('.')[0])
                        elif isinstance(node, ast.ImportFrom):
                            if node.level == 0 and node.module:
                                imports.add(node.module.split('.')[0])
    return imports

def get_requirements(filepath):
    if not os.path.exists(filepath):
        return set()
    with open(filepath, "r") as f:
        return {line.split('==')[0].split('>=')[0].strip().lower() for line in f if line.strip() and not line.startswith('#')}

def main():
    project_src = "src"
    req_file = "requirements.txt"
    
    used_modules = {m.lower() for m in get_imports(project_src)}
    declared_packages = get_requirements(req_file)

    std_lib = {'os', 'sys', 'ast', 'math', 'time', 'json', 're', 'datetime'} 
    used_external = used_modules - std_lib

    missing = used_external - declared_packages
    extra = declared_packages - used_external

    print(f"--- Анализ зависимостей ({project_src}) ---")
    if missing:
        print(f"ОТСУТСТВУЮТ в {req_file}: {', '.join(missing)}")
    if extra:
        print(f"ЛИШНИЕ в {req_file} (не найдены в коде): {', '.join(extra)}")
    
    if missing:
        sys.exit(1)
    print("Все импорты соответствуют требованиям.")

if __name__ == "__main__":
    main()
