pip install -r requirements.txt --break-system-packages
# clear
python3 -m PyInstaller --onefile main.py --add-data "GUI.py:." --distpath bin/
mv bin/main bin/ngif
rm -rf build
rm -rf dist
rm main.spec
# clear
echo Build done.
