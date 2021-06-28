@echo off
set PATH=C:\Users\Soonki\AppData\Local\Programs\Python\Python38-32;%PATH%
if not exist venv python -m venv venv
call venv\scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python -V
