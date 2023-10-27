# Log Periodic Power Law Singularity

LPPLS stands for Log-Periodic Power Law Singularity. It is a mathematical model used in the field of financial economics and complex systems to describe the behavior of financial market bubbles and crashes. The LPPLS model attempts to capture the speculative bubbles that can occur in financial markets, such as stock markets or cryptocurrency markets, and predict when they might burst.

The LPPLS model is based on the idea that during a financial bubble, the price of an asset (like a stock or cryptocurrency) increases at an accelerating rate, with oscillations or wavy patterns in the price chart. The model uses a mathematical formula with various parameters to fit the observed price data and make predictions about the likely time frame for the bubble to burst.

It's important to note that the LPPLS model is a subject of debate and criticism in the financial community. Some researchers and traders find it useful for identifying potential market crashes, while others consider it overly complex and not reliable for making investment decisions. Like many models in economics and finance, its predictive power is limited, and it may not always accurately forecast market behavior.


## Running

Create virtual environment 

`python3 -m venv .venv-lppls`

Activate virtual environment 

> Linux/MAC

`$ .venv-lppls/bin/activate`

> Windows
Command Prompt:

`> .venv-lppls\Scripts\activate`

PowerShell:

`PS> .\.venv-lppls\Scripts\Activate`


To run the notebook, run the folliwing command to add the virtual environment to jupyter kernel

`ipython kernel install --user --name=.venv-lppls`


Install the required packages in the `.venv-lppls`

`> pip install -r requirements.txt`

Deactivating the virtual environment

`$ deactivate` or `> deactivate`
