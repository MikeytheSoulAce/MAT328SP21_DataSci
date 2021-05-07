# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 22:14:36 2021

@author: mikem
"""

import matplotlib.pyplot as plt
import seaborn as sns

from Milestone_1 import covidnyc


def totaltests():
    """shows freq of COVID tests per neighborhood"""
    sns.histplot(data=covidnyc["TOTAL_COVID_TESTS"], kde=True)
    plt.xlabel("Total number of COVID-19 tests per neighborhood")
    plt.ylabel("Frequency")
    plt.title("Frequency of number of COVID-19 tests per neighborhood")


if __name__ == '__main__':
    totaltests()
