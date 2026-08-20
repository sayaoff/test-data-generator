#!/bin/bash

cd "$(dirname "$0")"

if ! command -v python3 >/dev/null 2>&1; then
    echo "Python 3 не найден. Установите его с https://www.python.org/downloads/macos/"
    echo
    echo "Нажмите Enter, чтобы закрыть окно..."
    read -r
    exit 1
fi

python3 web_app.py
status=$?

if [ $status -ne 0 ]; then
    echo
    echo "Не удалось запустить приложение."
    echo "Если порт 8765 занят, закройте другую копию программы и попробуйте снова."
    echo
    echo "Нажмите Enter, чтобы закрыть окно..."
    read -r
fi

exit $status
