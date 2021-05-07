#!/usr/bin/env python
# coding: utf-8

# Milestone 3a: Using Folium to create chloropleth maps for COVID-19 prevalence in NYC
# I am using Folium chloropleth map to illustrate the zones
# I had to grab the modified ZCTA data as a geojson in order to draw the borders of each modified ZCTA
# so that it would play nicely with the COVID data which uses the modified ZCTA.
# Modified ZCTAs are based on 2010 Census data.
# A detailed explanation for what modified ZCTAs are can be found on the project website.

import folium
import pandas as pd

zcta_boundaries = "../Modified Zip Code Tabulation Areas (MODZCTA).geojson"

# test map creation
covid_map = folium.Map(location=[40.6931703, -73.9524128])

# test drawing chloropleth map data
folium.Choropleth(geo_data=zcta_boundaries,
                  fill_opacity=0.5, line_opacity=0.5,
                  ).add_to(covid_map)

# COVID case count by modified ZCTA
covid_data = pd.read_csv("../data-by-modzcta.csv")

# realized that key in json is a string and key in csv is an int so convert to string needed
covid_data["MODIFIED_ZCTA"] = covid_data["MODIFIED_ZCTA"].astype(str)

covid_map = folium.Map(location=[40.6931703, -73.9524128])

folium.Choropleth(geo_data=zcta_boundaries,
                  fill_color='YlOrRd',
                  data=covid_data,
                  key_on="feature.properties.modzcta",
                  columns=['MODIFIED_ZCTA', 'COVID_CASE_COUNT'],
                  fill_opacity=0.5, line_opacity=0.5
                  ).add_to(covid_map)

covid_map.save("covidcasecount_modzcta.html")

# COVID death count by modified ZCTA
covid_map = folium.Map(location=[40.6931703, -73.9524128])

folium.Choropleth(geo_data=zcta_boundaries,
                  fill_color='YlOrRd',
                  data=covid_data,
                  key_on="feature.properties.modzcta",
                  columns=['MODIFIED_ZCTA', 'COVID_DEATH_COUNT'],
                  fill_opacity=0.5, line_opacity=0.5
                  ).add_to(covid_map)

covid_map.save("coviddeathcount_modzcta.html")

# COVID case rate by modified ZCTA
covid_map = folium.Map(location=[40.6931703, -73.9524128])

folium.Choropleth(geo_data=zcta_boundaries,
                  fill_color='YlOrRd',
                  data=covid_data,
                  key_on="feature.properties.modzcta",
                  columns=['MODIFIED_ZCTA', 'COVID_CASE_RATE'],
                  fill_opacity=0.5, line_opacity=0.5
                  ).add_to(covid_map)

covid_map.save("covidcaserate_modzcta.html")

# COVID death rate by modified ZCTA
covid_map = folium.Map(location=[40.6931703, -73.9524128])

folium.Choropleth(geo_data=zcta_boundaries,
                  fill_color='YlOrRd',
                  data=covid_data,
                  key_on="feature.properties.modzcta",
                  columns=['MODIFIED_ZCTA', 'COVID_DEATH_RATE'],
                  fill_opacity=0.5, line_opacity=0.5
                  ).add_to(covid_map)

covid_map.save("coviddeathrate_modzcta.html")

# percent positive by modified ZCTA
covid_map = folium.Map(location=[40.6931703, -73.9524128])

folium.Choropleth(geo_data=zcta_boundaries,
                  fill_color='YlOrRd',
                  data=covid_data,
                  key_on="feature.properties.modzcta",
                  columns=['MODIFIED_ZCTA', 'PERCENT_POSITIVE'],
                  fill_opacity=0.5, line_opacity=0.5
                  ).add_to(covid_map)

covid_map.save("pctpos_modzcta.html")
