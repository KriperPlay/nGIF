@echo off
SETLOCAL

pip install -r requirements.txt --break-system-packages
cls

python -m PyInstaller --onefile main.py --add-data "GUI.py;." --distpath bin/

move distmain.exe dist\ngif.exe

move dist\ngif.exe .

rmdir /S /Q build
rmdir /S /Q dist
del main.spec

cls

ENDLOCAL
echo Build done.
pause

