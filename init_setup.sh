echo [$(date)] "START"


echo [$(date)] "Creating the python 3.8 virtual environment"
conda create -p ./venv python=3.8 -y


echo [$(date)] "Activating python 3.8 virtual environment"
source activate ./venv


echo [$(date)] "Installing the requirments"
pip install -r requirements.txt


echo [$(date)] "END"