virtualenv venv
call venv\Scripts\activate.bat
pip install -r requirements.txt
pre-commit install
cmd.exe /k