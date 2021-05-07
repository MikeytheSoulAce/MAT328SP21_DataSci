import matplotlib.pyplot as plt
import pandas as pd

covidnyc = pd.read_csv("../data-by-modzcta.csv")

def main():
    from Milestone_1.borodeaths import borodeaths
    from Milestone_1.coviddeathrate import coviddeaths
    from Milestone_1.pctpos import pctpos
    from Milestone_1.postests import postests
    from Milestone_1.totalcases import totalcases
    from Milestone_1.totaltests import totaltests

    borodeaths()
    plt.figure()
    coviddeaths()
    plt.figure()
    pctpos()
    plt.figure()
    postests()
    plt.figure()
    totalcases()
    plt.figure()
    totaltests()

if __name__ == '__main__':
    main()
