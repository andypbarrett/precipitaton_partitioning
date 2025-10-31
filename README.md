# Precipitation Partitioning

This is a fork of Zaria Cast's Precip.-Partioning repo containing her code for her Masters Thesis 

## Contents

### ArcticMap.ipynb
Code to plot map of Arctic with regions named

### ERA5_Rainfall.ipynb
Does not generate figure

### ERA5-Test-landmask.ipynb
Example notebook.  Final calculations look wrong

### evaporation.ipynb
Plots evaporation and latent heat flux

### LandSeaMask.ipynb
No plot or functional code

### LiquidPrecip.ipynb


### LiquidPrecipONLY.ipynb


### STAYhere.ipynb
Does not seem relevant - some strange unit conversions

### temperature.ipynb
No plot

### TotalRainfall.ipynb
No plot

### TP-sf.ipynb

## Figures

### Figure 3: Spatial distribution of average annual totals (1973-2023) of total precipitation, snowfall, liquid precipitation and the liquid/total precipitation ratio from ERA5. Black contours are drawn on the figures for ease of viewing and occur every 200mm for the total precipitation, snowfall, and liquid precipitation and every 0.1 for the liquid/total precipitation plot in the lower right panel.

### Figure 4: Average annual totals of  precipitation, snowfall, and liquid precipitation for January (winter; (top) and July (summer; (bottom) from ERA5 (1979–2023).

### Figure 5: Average latent heat fluxes for winter and summer, 1979-2023, from ERA5. These are created by using monthly averages of hourly data.

### Figure 6: Average seasonal distribution of the liquidrainfall-to-total precipitation ratio from ERA5, 1979 to 2023.
LiquidPrecip: code cell 89

### Figure 10: Linear trends in annual total precipitation, snowfall, and liquid precipitation from 1979 to 2023 from ERA5. Only trends that are statistically significant at the 95% confidence level are shown by colors.

### Figure 11: The difference in annual liquid precipitation between the recent period (2013–2023) and an earlier baseline period (1979–1989) from ERA5.

```
# Calculate liquid precip

```
```
# Selecting the data for the first and last decades
first_decade = liquid_precip.sel(date=slice('1979-01-01', '1989-12-31'))
last_decade = liquid_precip.sel(date=slice('2013-01-01', '2023-12-31'))

# Compute the mean liquid precipitation for each decade
first_decade_mean = first_decade.mean(dim='date')
last_decade_mean = last_decade.mean(dim='date')

# Calculate the difference between the last and first decade and multiply by 1000
lp_difference = (last_decade_mean - first_decade_mean) * 1000  # Converts to mm if data is in meters
```

### Figure 12: Seasonal trends in liquidrainfall to total precipitation ratios (1979–2023) from ERA5. Only trends that are statistically significant at the 95% confidence level are shown by colors.

