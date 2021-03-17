# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 01:05:44 2021

@author: mikem
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

covidnyc = pd.read_csv("data-by-modzcta.csv")

def postests():
    
    sns.regplot(x = "TOTAL_COVID_TESTS", y = "PERCENT_POSITIVE", data = covidnyc)
    plt.title("Scatter plot of total COVID-19 tests with percent of positive cases")
    plt.xlabel("Total number of COVID tests")
    plt.ylabel("Percentage of positive COVID-19 tests")

postests()
