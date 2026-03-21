
## Problem
Ручное управление окружением и проверками неудобно и невоспроизводимо.

## Solution
Использование Makefile как точки входа для всех действий.

## Virtual Environment
Почему используется .venv/bin/python вместо activate:
- Make не сохраняет shell
- явные пути надёжнее

## Dependency Management
Реализован скрипт, который:
- анализирует импорты
- сравнивает с requirements.txt