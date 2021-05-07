(lambda
 pd=__import__("pandas"),
 sns=__import__("seaborn"),
 plt=__import__("matplotlib.pyplot").pyplot:
 (lambda covidnyc=pd.read_csv("../data-by-modzcta.csv"):
  (lambda **kwargs: [f() for f in (
      kwargs["borodeaths"], plt.figure,
      kwargs["coviddeaths"], plt.figure,
      kwargs["pctpos"], plt.figure,
      kwargs["postests"], plt.figure,
      kwargs["totalcases"], plt.figure,
      kwargs["totaltests"], plt.show)])(
      coviddeaths=lambda: [f() for f in (
          (lambda: sns.histplot(data=covidnyc["COVID_DEATH_RATE"], kde=True)),
          (lambda: plt.ylabel("Frequency")),
          (lambda: plt.xlabel("Number of deaths from COVID-19 per neighborhood")),
          (lambda: plt.title("Frequency of deaths from COVID-19 in each neighborhood")))],
      postests=lambda: [f() for f in (
          (lambda: sns.regplot(x="TOTAL_COVID_TESTS", y="PERCENT_POSITIVE", data=covidnyc)),
          (lambda: plt.xlabel("Total number of COVID tests")),
          (lambda: plt.ylabel("Percentage of positive COVID-19 tests")),
          (lambda: plt.title("Scatter plot of total COVID-19 tests with percent of positive cases")))],
      totalcases=lambda: [f() for f in (
          (lambda: sns.histplot(data=covidnyc["COVID_CASE_COUNT"], kde=True)),
          (lambda: plt.ylabel("Frequency")),
          (lambda: plt.xlabel("Total number of COVID-19 cases per neighborhood")),
          (lambda: plt.title("Frequency of total number of COVID-19 cases per neighborhood")))],
      pctpos=lambda: [f() for f in (
          (lambda: sns.histplot(data=covidnyc["PERCENT_POSITIVE"], kde=True)),
          (lambda: plt.ylabel("Frequency")),
          (lambda: plt.xlabel("Percent of residents per neighborhood tested positive for COVID-19")),
          (lambda: plt.title(
              "Frequency of percentages of residents in each neighborhood who tested positive for COVID-19")))],
      totaltests=lambda: [f() for f in (
          (lambda: sns.histplot(data=covidnyc["TOTAL_COVID_TESTS"], kde=True)),
          (lambda: plt.ylabel("Frequency")),
          (lambda: plt.xlabel("Total number of COVID-19 tests per neighborhood")),
          (lambda: plt.title("Frequency of number of COVID-19 tests per neighborhood")))],
      borodeaths=lambda: [f() for f in (
          (lambda: sns.catplot(x="BOROUGH_GROUP", y="COVID_DEATH_COUNT",
                               kind="box", data=covidnyc).fig.set_size_inches(6, 6)),
          (lambda: plt.xlabel("Borough")),
          (lambda: plt.title("Boxplot of deaths from COVID-19 by borough")),
          (lambda: plt.ylabel("Number of deaths")))]))())()
