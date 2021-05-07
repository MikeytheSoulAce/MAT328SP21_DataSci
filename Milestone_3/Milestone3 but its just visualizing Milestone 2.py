import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression as LinReg
from sklearn.preprocessing import PolynomialFeatures as PolyReg
from sklearn.tree import DecisionTreeRegressor as DTreeReg

covidnyc = pd.read_csv("../data-by-modzcta.csv")

x_train = covidnyc[["lat", "lon"]]
y_train = covidnyc["COVID_CASE_RATE"]

poly_2 = PolyReg(degree=2)
lin_2 = LinReg().fit(poly_2.fit_transform(x_train), y_train)

poly_5 = PolyReg(degree=5)
lin_5 = LinReg().fit(poly_5.fit_transform(x_train), y_train)

poly_10 = PolyReg(degree=10)
lin_10 = LinReg().fit(poly_10.fit_transform(x_train), y_train)

dtree_3 = DTreeReg(max_depth=3).fit(x_train, y_train)
dtree_6 = DTreeReg(max_depth=6).fit(x_train, y_train)
dtree_10 = DTreeReg(max_depth=10).fit(x_train, y_train)


def stringify(xy: np.ndarray):
    return np.array(list(map(str, xy)))


def poly(lin, pol):
    return lambda xy: lin.predict(pol.fit_transform(xy))


def make_grid(x_min, x_max, y_min, y_max, x_dim, y_dim):
    xs, ys = divmod(np.arange(x_dim * y_dim).reshape((x_dim * y_dim, 1)), y_dim)

    xs = x_min + xs * (x_max - x_min) / x_dim
    ys = y_min + ys * (y_max - y_min) / y_dim

    return np.concatenate((xs, ys), axis=1)


latmin, lonmin = x_train.min().to_list()
latmax, lonmax = x_train.max().to_list()

def formataxis(axis):
    ticks = axis.get_majorticklocs()
    formatter = axis.get_major_formatter()
    labels = formatter.format_ticks(ticks)
    for i, x in enumerate(labels):
        labels[i] = f"{float(x):.4g}"
    offset = formatter.get_offset()
    axis.set_ticklabels(labels)
    axis.get_major_formatter().set_offset_string(offset)


def heatmap(color, title=""):
    fig = plt.figure()
    y, x = color.shape
    color = pd.DataFrame(color,
                         index=np.arange(latmin, latmax, (latmax - latmin) / y),
                         columns=np.arange(lonmin, lonmax, (lonmax - lonmin) / x))

    sns.heatmap(color, square=True)
    formataxis(fig.axes[0].xaxis)
    formataxis(fig.axes[0].yaxis)

    fig.axes[0].set_title(title)
    fig.axes[0].set_xlabel('longitude')
    fig.axes[0].set_ylabel('latitude')
    fig.axes[1].set_ylabel('covid case rate')

    return fig


size = (100, 100)
heatmap_input = make_grid(latmin, latmax, lonmin, lonmax, *size)
heatmap(poly(lin_2, poly_2)(heatmap_input).reshape(size), "poly 2")
heatmap(poly(lin_5, poly_5)(heatmap_input).reshape(size), "poly 5")
heatmap(poly(lin_10, poly_10)(heatmap_input).reshape(size), "poly 10")
heatmap(dtree_3.predict(heatmap_input).reshape(size), "tree 3")
heatmap(dtree_6.predict(heatmap_input).reshape(size), "tree 6")
heatmap(dtree_10.predict(heatmap_input).reshape(size), "tree 10")
