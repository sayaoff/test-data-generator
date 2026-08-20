@echo off
cd /d "%~dp0"
python web_app.py
if errorlevel 1 (
    echo.
    echo Не удалось запустить программу. Убедитесь, что Python установлен.
    pause
)
