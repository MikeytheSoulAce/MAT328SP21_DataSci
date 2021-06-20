(lambda folium=__import__("folium"),
        pd=__import__("pandas"):
 lambda zcta_boundaries="../Modified Zip Code Tabulation Areas (MODZCTA).geojson",
         covid_data=(lambda cd=pd.read_csv("../data-by-modzcta.csv"):
                     [cd.__setitem__("MODIFIED_ZCTA", cd["MODIFIED_ZCTA"].astype(str)), cd][1])():
  [(lambda: folium.Choropleth(geo_data=zcta_boundaries, fill_color='YlOrRd', data=covid_data,
                              fill_opacity=0.5, line_opacity=0.5,
                              key_on="feature.properties.modzcta", columns=['MODIFIED_ZCTA', column]
                              ).add_to(folium.Map(location=[40.6931703, -73.9524128]))._parent.save(export))()
   for column, export in [('COVID_CASE_COUNT', "covidcasecount_modzcta.html"),
                          ('COVID_DEATH_COUNT', "coviddeathcount_modzcta.html"),
                          ('COVID_CASE_RATE', "covidcaserate_modzcta.html"),
                          ('COVID_DEATH_RATE', "coviddeathrate_modzcta.html"),
                          ('PERCENT_POSITIVE', "pctpos_modzcta.html")]])()()
