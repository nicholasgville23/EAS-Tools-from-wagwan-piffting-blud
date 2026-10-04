@echo off
py -3 -m pip install --upgrade pyinstaller
py -3 -m PyInstaller --noconfirm --clean --onefile --windowed --name KLOT_LOTIEM_EAS_BMH app.py
pause
