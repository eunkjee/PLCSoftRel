venv_name=venv

# install miniconda
echo INFO: Start installing Miniconda...
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
echo INFO: Miniconda installation finished.

# activate miniconda
~/miniconda3/bin/conda init bash
echo INFO: Miniconda activated.

# create and activate a virtual environment
echo INFO: Start creating the virtual environment $venv_name...
conda create -c conda-forge -p .\venv "pymc=5.11.0"
conda activate .\venv
echo INFO: The virtual environment $venv_name activated.

# install the required packages
echo INFO: Start installing the required packages...
pip install -r requirements.txt
echo INFO: The installation of required packages finished.
