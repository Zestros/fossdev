.PHONY: another-app

# не совпадение build и имени выходного файла приведет к перекомпиляции
build: main.c
	gcc main.c -o app
# совпадает поэтому будет проверять измененеие и не перекомпилировать
app: main.c
	gcc main.c -o app

# тк .PHONY все равно перекомпилирует (отключает зависимости файловой системы)
another-app: main.c
	gcc main.c -o another-app
