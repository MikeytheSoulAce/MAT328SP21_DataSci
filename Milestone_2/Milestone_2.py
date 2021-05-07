"""
Milestone 2 of the data project
For this milestone I am doing linear and decision tree regression on the COVID-19 data in NYC.
"""

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split as tts

from sklearn.tree import DecisionTreeRegressor as DTreeReg
from sklearn.preprocessing import PolynomialFeatures as PolyReg
from sklearn.linear_model import LinearRegression as LinReg

from sklearn.metrics import mean_squared_error as mse

covidnyc = pd.read_csv("../data-by-modzcta.csv")

x = covidnyc[["lat", "lon"]]
y = covidnyc["COVID_CASE_RATE"]

random_state = None
if random_state is None:
    random_state = np.random.randint(np.iinfo(np.int32).max)
print("random state:", random_state, "selected as random state integer for test/train splitting")
x_train, x_test, y_train, y_test = tts(x, y, test_size=0.2, random_state=random_state)

# degree 2 polynomial
poly_2 = PolyReg(degree=2)
lin_2 = LinReg().fit(poly_2.fit_transform(x_train), y_train)
print("degree  2 polynomial:",
      mse(y_test, lin_2.predict(poly_2.fit_transform(x_test))))
# 1537322.3403298033

# degree 5 polynomial
poly_5 = PolyReg(degree=5)
lin_5 = LinReg().fit(poly_5.fit_transform(x_train), y_train)
print("degree  5 polynomial:",
      mse(y_test, lin_5.predict(poly_5.fit_transform(x_test))))
# 2945107.6436907398

# degree 10 polynomial
poly_10 = PolyReg(degree=10)
lin_10 = LinReg().fit(poly_10.fit_transform(x_train), y_train)
print("degree 10 polynomial:",
      mse(y_test, lin_10.predict(poly_10.fit_transform(x_test))))
# 1975027.9526580998

# depth 3 tree
dtree_3 = DTreeReg(max_depth=3).fit(x_train, y_train)
print("depth   3       tree:",
      mse(y_test, dtree_3.predict(x_test)))
# 1698269.240266402

# depth 6 tree
dtree_6 = DTreeReg(max_depth=6).fit(x_train, y_train)
print("depth   6       tree:",
      mse(y_test, dtree_6.predict(x_test)))
# 1599419.3151484672

# depth 10 tree
dtree_10 = DTreeReg(max_depth=10).fit(x_train, y_train)
print("depth  10       tree:",
      mse(y_test, dtree_10.predict(x_test)))
# 1832320.6709397873
