@echo off
REM Activate the virtual environment and run the script automatically
cd /d "%~dp0"
call .venv\Scripts\activate.bat
python stockprediction.py
