# Log Periodic Power Law Singularity

[![Python 3](https://img.shields.io/badge/python-3-blue?style=for-the-badge&logo=python)](https://www.python.org/)

LPPLS stands for Log-Periodic Power Law Singularity. It is a mathematical model used in the field of financial economics and complex systems to describe the behavior of financial market bubbles and crashes. The LPPLS model attempts to capture the speculative bubbles that can occur in financial markets, such as stock markets or cryptocurrency markets, and predict when they might burst.

The LPPLS model is based on the idea that during a financial bubble, the price of an asset (like a stock or cryptocurrency) increases at an accelerating rate, with oscillations or wavy patterns in the price chart. The model uses a mathematical formula with various parameters to fit the observed price data and make predictions about the likely time frame for the bubble to burst.

It's important to note that the LPPLS model is a subject of debate and criticism in the financial community. Some researchers and traders find it useful for identifying potential market crashes, while others consider it overly complex and not reliable for making investment decisions. Like many models in economics and finance, its predictive power is limited, and it may not always accurately forecast market behavior.


## How to Use

### 1. Global installation

1. Clone the repository:
   ```bash
   git clone https://github.com/cmosongo/lppls.git
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Jupyter notebook:
   ```bash
   jupyter notebook notebooks/LPPLS.ipynb
   ```

## 2. Virtual Environment

Clone the repository and navigate to the parent folder using either the Command Prompt `cmd` or PowerShell on Windows, or any Unix-based terminal. Then, run the following commands:

1. Create virtual environment 
	```bash
	python3 -m venv .venv
	```

2. Activate virtual environment 

	> Unix
	```bash
	$ source .venv/bin/activate
	```

	> Windows
	Command Prompt:
	```bash
	> .venv\Scripts\activate
	```

	PowerShell:
	```shell
	PS> .\.venv\Scripts\Activate
	```

3. To use nootebooks:

	```bash
	(.venv)> pip install ipykernel
	```

4. To run the notebook, run the following command to add the virtual environment to jupyter kernel

	```bash
	(.venv)> python -m ipykernel install --user --name=.venv --display-name "LPPLS Analysis"
	```

5. Install the required packages 
	```bash
	(.venv)> pip install -r requirements.txt
	```

6. Deactivating the virtual environment

	 ```bash
	 deactivate
	 ```

`> pip install -r requirements.txt`

Deactivating the virtual environment

`$ deactivate` or `> deactivate`
