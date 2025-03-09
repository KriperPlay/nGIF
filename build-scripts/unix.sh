pip install -r requirements.txt
clear
python3 -m PyInstaller --onefile main.py --add-data "GUI.py:." --distpath bin/
mv dist/main dist/ngif
mv dist/ngif ./
rm -rf build
rm -rf dist
rm main.spec
clear
echo Build done.
