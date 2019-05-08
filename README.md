# Auto BPM
This tiny script opens bronze packs automatically, until you stop it.

# NOTE
I created this script only for myself. This was not intended to be released to the public. There ~~might~~ *will* be bugs. This script has only been tested on Mac OSX.

# Requirements
1. Chrome (I'm assuming you already have this)
2. Python
3. Pip

# Installation

First of all, download a zip of this repo [here](https://github.com/shikharg3/BPM/archive/master.zip) or by clicking 'Clone or download' on the top right and extract it.

## Windows
### Install Python
1. Download installer for your OS from [here](https://www.python.org/downloads/release/python-2716/)
2. Add Python to PATH. Follow [this tutorial](https://datatofish.com/add-python-to-windows-path/)
3. Open cmd and type python, if you don't see an error, python is succesfully installed.

### Install PIP
We need pip to install the libraries used.
1. Download get-pip.py from [here](https://bootstrap.pypa.io/get-pip.py)
2. Open cmd in the folder of get-pip.py and type following command ```python get-pip.py```

### Install Libraries
Once pip is installed, open cmd, cd to the folder where requirements.txt is located and type (in cmd) ```pip install -r requirements.txt```

## Mac
Python comes pre-installed so you can skip that part.

### Install PIP
We need pip to install the libraries used.
1. Download get-pip.py from [here](https://bootstrap.pypa.io/get-pip.py)
2. Open terminal (goto where get-pip.py is located) and type following command ```python get-pip.py```

### Install Libraries
Once pip is installed, open terminal, cd to the folder where requirements.txt is located and type (in terminal) ```sudo pip install -r requirements.txt```

# Using the script
1. Open cmd/terminal in your project directory and type ```sudo python bpm.py```
2. A chrome window will open and the webapp will load. Login to the webapp and go to the packs section.
3. Now press 'space bar' and the script will start ripping open bronze packs.
4. To stop the script, press ctrl+c or ctrl+z in cmd/terminal. Or close the terminal/cmd window.

# Known Bugs
1. Sometimes free packs are not redeemed. In this case you need to manually click on 'redeem'

