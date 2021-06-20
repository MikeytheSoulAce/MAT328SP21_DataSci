# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 22:25:21 2021

@author: mikem
"""

import matplotlib.pyplot as plt
import seaborn as sns

from Milestone_1 import covidnyc


def totalcases():
    """shows freq of total number of COVID-19 cases per neighborhood"""
    sns.histplot(data=covidnyc["COVID_CASE_COUNT"], kde=True)
    plt.xlabel("Total number of COVID-19 cases per neighborhood")
    plt.ylabel("Frequency")
    plt.title("Frequency of total number of COVID-19 cases per neighborhood")


if __name__ == '__main__':
    totalcases()
