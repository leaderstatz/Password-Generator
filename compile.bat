@echo off

CALL .venv/scripts/activate.bat

pyinstaller --onefile --noconsole --icon=assets/lock.ico --add-data "assets/lock.ico;assets/lock.ico" app.py

del /q "app.spec"
rmdir /s /q "build"