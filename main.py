import numpy as np
import pandas as pd
import yfinance as yf
from lppls import lppls, data_loader
from datetime import datetime as dt

ticker = '^GSPC'
start = '2015-01-01'
end = '2022-07-31'
data = yf.download(ticker, start=start, end=end)
print(data.info())


time = [pd.Timestamp.toordinal(t1) for t1 in (data.index).date]
# create list of observation data
price = np.log(data['Adj Close'].values)


# create observations array (expected format for LPPLS observations)
observations = np.array([time, price])

# set the max number for searches to perform before giving-up
# the literature suggests 25
MAX_SEARCHES = 25

# instantiate a new LPPLS model with the Nasdaq Dot-com bubble dataset
lppls_model = lppls.LPPLS(observations=observations)

# fit the model to the data and get back the params
tc, m, w, a, b, c, c1, c2, O, D = lppls_model.fit(MAX_SEARCHES)

# visualize the fit
lppls_model.plot_fit()

# compute the confidence indicator
res = lppls_model.mp_compute_nested_fits(
    workers=8,
    window_size=120, 
    smallest_window_size=30, 
    outer_increment=1, 
    inner_increment=5, 
    max_searches=25,
    # filter_conditions_config={} # not implemented in 0.6.x
)

lppls_model.plot_confidence_indicators(res)
# should give a plot like the following...
