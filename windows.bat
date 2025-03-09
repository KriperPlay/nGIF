@echo off
SETLOCAL

pip install -r requirements.txt
cls

python -m PyInstaller --onefile main.py --add-data "GUI.py;." --distpath bin/

move bin\main.exe bin\ngif.exe

rmdir /S /Q build
rmdir /S /Q dist
del main.spec

cls

ENDLOCAL
echo Build done.
pause

