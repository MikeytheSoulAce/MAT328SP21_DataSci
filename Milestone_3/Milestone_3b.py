#!/usr/bin/env python
# coding: utf-8

# Milestone 3b: Pairplot by borough, heatmap, and pairplot with contour plot for COVID-19 data
# I couldn't decide on what I wanted to use for this submission, so I decided on a few things.

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

covid_data = pd.read_csv("../data-by-modzcta.csv")

# standard pairplot with relevant quantitative columns
sns.pairplot(data=covid_data,
             vars=["COVID_CASE_COUNT", "COVID_CASE_RATE", "COVID_DEATH_COUNT",
                   "COVID_DEATH_RATE", "PERCENT_POSITIVE", "TOTAL_COVID_TESTS"],
             hue="BOROUGH_GROUP")

# Interesting graph that depicts lat/long of ZCTAs
sns.pairplot(data=covid_data, vars=["lat", "lon"], hue="BOROUGH_GROUP")

plt.figure()
# Heatmap of all quantitative columns
sns.heatmap(covid_data.corr())

# using PairGrid to draw
g = sns.PairGrid(covid_data,
                 vars=["COVID_CASE_COUNT", "COVID_CASE_RATE", "COVID_DEATH_COUNT",
                       "COVID_DEATH_RATE", "PERCENT_POSITIVE", "TOTAL_COVID_TESTS"],
                 diag_sharey=False)
g.map_upper(sns.scatterplot, s=15)
g.map_lower(sns.kdeplot)
g.map_diag(sns.kdeplot, lw=2)
