venv_name=venv

# install miniconda
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh

# activate miniconda
~/miniconda3/bin/conda init bash

# create and activate a virtual environment
conda create -c conda-forge -p .\venv "pymc=5.11.0"
conda activate .\venv

# install the required packages
pip install -r requirements.txt
