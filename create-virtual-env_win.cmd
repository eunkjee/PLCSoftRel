set venv_name=venv

:: install miniconda
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o miniconda.exe
start /wait "" miniconda.exe /S
del miniconda.exe

:: activate miniconda
call %USERPROFILE%\miniconda3\Scripts\activate.bat %USERPROFILE%\miniconda3

:: create and activate a virtual environment
call conda create -c conda-forge -p .\%venv_name% "pymc=5.11.0" -y
call conda activate .\%venv_name%

:: install the required packages
pip install -r requirements.txt
