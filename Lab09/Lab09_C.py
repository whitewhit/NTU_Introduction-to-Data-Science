import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from scipy.optimize import curve_fit
from sklearn.metrics import mean_squared_error

# the fouction of market_value
def market_value(df, b0, b1, b2, b3, b4, b5, b6, b7):
    market = b0 + b1*df[:, 0] + b2*df[:, 1] + b3*df[:, 2]+ b4*df[:, 3] + b5*df[:, 4] + b6*df[:, 5] + b7*df[:, 6]
    return market.flatten()

df = pd.read_csv('epldata_final.csv')

X = df.filter(['fpl_value', 'age', 'age', 'page_views',\
            'new_signing', 'big_club', 'position_cat']).to_numpy()

y = df.filter(['market_value']).to_numpy()

for i in X:
    i[2] = pow(i[2], 2)
    i[3] = np.log2(i[3])

# split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=104,test_size=0.2, shuffle=True)

# find the coefficients of market_value curve
coefficients, _ = curve_fit(market_value, X_train, y_train.flatten())

b0, b1, b2, b3, b4, b5, b6, b7 = coefficients
print('coefficients= ', coefficients)

# use x_test data find y_predict
y_predit =  market_value(X_test, b0, b1, b2, b3, b4, b5, b6, b7)

# the mse of y_predit amd y_test
mse = mean_squared_error(y_predit, y_test)
print('mse= ', mse)
