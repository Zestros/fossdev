## Разработка

### До Make:
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

### После Make:
make venv
make install
make check

## Virtual Environment
Почему используется .venv/bin/python вместо activate:
- Make не сохраняет shell
- явные пути надёжнее

## Type Checking
Для статической проверки типов используется инструмент mypy.

Targets, использующие инструменты mypy, зависят от install,
чтобы гарантировать наличие всех зависимостей перед выполнением.

## Code Style
Для форматирования используется black.
Два режима работы:
- проверка
- автоматическое исправление
