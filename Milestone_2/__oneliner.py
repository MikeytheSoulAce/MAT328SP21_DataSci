(lambda
 pd=__import__('pandas'),
 np=__import__('numpy'),
 tts=__import__("sklearn.model_selection", fromlist=[""]).train_test_split,
 DTreeReg=__import__("sklearn.tree", fromlist=[""]).DecisionTreeRegressor,
 PolyReg=__import__("sklearn.preprocessing", fromlist=[""]).PolynomialFeatures,
 LinReg=__import__("sklearn.linear_model", fromlist=[""]).LinearRegression,
 mse=__import__("sklearn.metrics", fromlist=[""]).mean_squared_error:
 (lambda
  covidnyc=pd.read_csv("../data-by-modzcta.csv"),
  random_state=None or np.random.randint(np.iinfo(np.int32).max):
  [print("random state:", random_state, "selected as random state integer for test/train splitting"),
   (lambda x_train, x_test, y_train, y_test:
    (lambda display=lambda string, y_pred: print(string, mse(y_test, y_pred)):
     [display(f"degree {n:2d} polynomial:", (LinReg().fit(
         (poly_n := PolyReg(degree=n)).fit_transform(x_train), y_train)).predict(poly_n.fit_transform(x_test)))
      for n in (2, 5, 10)] +
     [display(f"depth  {n:2d}       tree:", (DTreeReg(max_depth=n).fit(x_train, y_train)).predict(x_test))
      for n in (3, 6, 10)])())(
       *tts(covidnyc[["lat", "lon"]], covidnyc["COVID_CASE_RATE"], test_size=0.2, random_state=random_state))])())()
