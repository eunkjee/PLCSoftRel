set venv_name=venv

:: activate miniconda
call %USERPROFILE%\miniconda3\Scripts\activate.bat %USERPROFILE%\miniconda3
echo INFO: Miniconda activated.

:: activate virtual environment
call conda activate .\%venv_name%
echo INFO: The virtual environment %venv_name% activated.

:: run server
cd server
echo INFO: Start running the server...
uvicorn main:app --reload --host=0.0.0.0 --port=8000
