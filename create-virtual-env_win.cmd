set venv_name=venv

:: install miniconda
echo INFO: Start installing Miniconda...
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o miniconda.exe
start /wait "" miniconda.exe /S
del miniconda.exe
echo INFO: Miniconda installation finished.

:: activate miniconda
call %USERPROFILE%\miniconda3\Scripts\activate.bat %USERPROFILE%\miniconda3
echo INFO: Miniconda activated.

:: create and activate a virtual environment
echo INFO: Start creating the virtual environment %venv_name%...
call conda create -c conda-forge -p .\%venv_name% "pymc=5.11.0" -y
call conda activate .\%venv_name%
echo INFO: The virtual environment %venv_name% activated.

:: install the required packages
echo INFO: Start installing the required packages...
pip install -r requirements.txt
echo INFO: The installation of required packages finished.
