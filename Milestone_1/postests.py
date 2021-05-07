# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 01:05:44 2021

@author: mikem
"""

import matplotlib.pyplot as plt
import seaborn as sns

from Milestone_1 import covidnyc


def postests():
    sns.regplot(x="TOTAL_COVID_TESTS", y="PERCENT_POSITIVE", data=covidnyc)
    plt.title("Scatter plot of total COVID-19 tests with percent of positive cases")
    plt.xlabel("Total number of COVID tests")
    plt.ylabel("Percentage of positive COVID-19 tests")


if __name__ == '__main__':
    postests()
