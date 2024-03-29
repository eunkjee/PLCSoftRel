set venv_name=venv

:: activate miniconda
call %USERPROFILE%\miniconda3\Scripts\activate.bat %USERPROFILE%\miniconda3

:: activate virtual environment
call conda activate .\%venv_name%

:: run server
cd server
uvicorn main:app --reload --host=0.0.0.0 --port=8000
