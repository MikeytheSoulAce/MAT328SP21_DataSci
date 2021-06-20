(lambda
 pd=__import__("pandas"),
 sns=__import__("seaborn"),
 plt=__import__("matplotlib.pyplot").pyplot:
 (lambda
  covidnyc=pd.read_csv("../data-by-modzcta.csv"),
  pltlabel_and_title=(lambda ylabel, xlabel, title: [plt.ylabel(ylabel), plt.xlabel(xlabel), plt.title(title)]):
  (lambda **kwargs: [
      kwargs["borodeaths"](), plt.figure(),
      kwargs["coviddeaths"](), plt.figure(),
      kwargs["pctpos"](), plt.figure(),
      kwargs["postests"](), plt.figure(),
      kwargs["totalcases"](), plt.figure(),
      kwargs["totaltests"](), plt.show()])(
      coviddeaths=lambda: [
          (sns.histplot(data=covidnyc["COVID_DEATH_RATE"], kde=True)),
          (pltlabel_and_title(
              "Frequency",
              "Number of deaths from COVID-19 per neighborhood",
              "Frequency of deaths from COVID-19 in each neighborhood"))],
      postests=lambda: [
          (sns.regplot(x="TOTAL_COVID_TESTS", y="PERCENT_POSITIVE", data=covidnyc)),
          (pltlabel_and_title(
              "Percentage of positive COVID-19 tests",
              "Total number of COVID tests",
              "Scatter plot of total COVID-19 tests with percent of positive cases"))],
      totalcases=lambda: [
          (sns.histplot(data=covidnyc["COVID_CASE_COUNT"], kde=True)),
          (pltlabel_and_title(
              "Frequency",
              "Total number of COVID-19 cases per neighborhood",
              "Frequency of total number of COVID-19 cases per neighborhood"))],
      pctpos=lambda: [
          (sns.histplot(data=covidnyc["PERCENT_POSITIVE"], kde=True)),
          (pltlabel_and_title(
              "Frequency",
              "Percent of residents per neighborhood tested positive for COVID-19",
              "Frequency of percentages of residents in each neighborhood who tested positive for COVID-19"))],
      totaltests=lambda: [
          (sns.histplot(data=covidnyc["TOTAL_COVID_TESTS"], kde=True)),
          (pltlabel_and_title(
              "Frequency",
              "Total number of COVID-19 tests per neighborhood",
              "Frequency of number of COVID-19 tests per neighborhood"))],
      borodeaths=lambda: [
          (sns.catplot(x="BOROUGH_GROUP", y="COVID_DEATH_COUNT", kind="box", data=covidnyc).fig.set_size_inches(6, 6)),
          (pltlabel_and_title(
              "Number of deaths",
              "Borough",
              "Boxplot of deaths from COVID-19 by borough"))]))())()
