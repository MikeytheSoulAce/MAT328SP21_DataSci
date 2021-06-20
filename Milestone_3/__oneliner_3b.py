(lambda pd=__import__("pandas"),
        sns=__import__("seaborn"):
 lambda covid_data=pd.read_csv("../data-by-modzcta.csv"),
        _vars=["COVID_CASE_COUNT", "COVID_CASE_RATE", "COVID_DEATH_COUNT",
               "COVID_DEATH_RATE", "PERCENT_POSITIVE", "TOTAL_COVID_TESTS"]:
 [sns.heatmap(covid_data.corr()),
  sns.pairplot(data=covid_data, vars=_vars, hue="BOROUGH_GROUP"),
  sns.pairplot(data=covid_data, vars=["lat", "lon"], hue="BOROUGH_GROUP"),
  sns.PairGrid(covid_data, vars=_vars, diag_sharey=False).map_upper(
      sns.scatterplot, s=15).map_lower(
      sns.kdeplot).map_diag(
      sns.kdeplot, lw=2)])()()
