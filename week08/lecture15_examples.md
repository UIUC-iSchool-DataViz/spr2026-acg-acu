---
jupytext:
  cell_metadata_filter: -all
  formats: ipynb,py:percent,md:myst
  notebook_metadata_filter: layout,title
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.0
kernelspec:
  display_name: Python 3
  language: python
  name: python3
layout: notebook
title: Lecture15 Examples
---

```{code-cell} ipython3
import cartopy
import matplotlib.pyplot as plt
```

```{code-cell} ipython3
fig = plt.figure()
ax = fig.add_subplot(111, projection=cartopy.crs.Mollweide())
ax.coastlines()
```

```{code-cell} ipython3
fig = plt.figure()
ax = fig.add_subplot(111, projection=cartopy.crs.Mollweide(central_longitude=180))
ax.coastlines()
```

```{code-cell} ipython3
fig = plt.figure()
ax = fig.add_subplot(111, projection=cartopy.crs.Orthographic())
ax.coastlines()
```

```{code-cell} ipython3
fig = plt.figure()
ax = fig.add_subplot(111, projection=cartopy.crs.PlateCarree())
ax.coastlines()
ax.gridlines()
```

```{code-cell} ipython3
c_lat, c_lon = 40.1164, -88.2434
a_lat, a_lon = -18.8792, 47.5079
fig = plt.figure(dpi=150)
ax = fig.add_subplot(111, projection=cartopy.crs.PlateCarree())
ax.scatter([c_lon, a_lon], [c_lat, a_lat])
ax.coastlines()
ax.gridlines()
ax.set_global()
```

```{code-cell} ipython3
c_lat, c_lon = 40.1164, -88.2434
a_lat, a_lon = -18.8792, 47.5079
fig = plt.figure(dpi=150)
ax = fig.add_subplot(111, projection=cartopy.crs.Mollweide())
ax.plot([c_lon, a_lon], [c_lat, a_lat], transform=cartopy.crs.PlateCarree())
ax.plot([c_lon, a_lon], [c_lat, a_lat], transform=cartopy.crs.Geodetic())
ax.coastlines()
ax.gridlines()
ax.set_global()
```

```{code-cell} ipython3
import numpy as np
vals = np.random.random((128, 128))
```

```{code-cell} ipython3
plt.imshow(vals)
```

```{code-cell} ipython3
c_lat, c_lon = 40.1164, -88.2434
a_lat, a_lon = -18.8792, 47.5079
fig = plt.figure(dpi=150)
ax = fig.add_subplot(111, projection=cartopy.crs.Mollweide())
ax.plot([c_lon, a_lon], [c_lat, a_lat], transform=cartopy.crs.PlateCarree())
ax.plot([c_lon, a_lon], [c_lat, a_lat], transform=cartopy.crs.Geodetic())
ax.imshow(vals, extent = [-60, -30, 30, 60], transform = cartopy.crs.PlateCarree())
ax.coastlines()
ax.gridlines()
ax.set_global()
```

```{code-cell} ipython3
import pandas as pd
```

```{code-cell} ipython3
!rm -f us-counties.csv ; wget https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv
```

```{code-cell} ipython3
!rm -f us-states.csv ; wget https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv
```

```{code-cell} ipython3
states = pd.read_csv("us-states.csv", parse_dates = ["date"])
```

```{code-cell} ipython3
import bqplot
```

```{code-cell} ipython3
proj = bqplot.AlbersUSA()
mark = bqplot.Map(map_data = bqplot.topo_load("map_data/USStatesMap.json"),
                  scales = {'projection': proj})
fig = bqplot.Figure(marks = [mark])
display(fig)
```

```{code-cell} ipython3
case_counts = states.groupby("fips")["cases"].max().to_dict()

proj = bqplot.AlbersUSA()
color_sc = bqplot.ColorScale(scheme = "viridis")
color_ax = bqplot.ColorAxis(scale = color_sc, label = 'Case Count')

mark = bqplot.Map(map_data = bqplot.topo_load("map_data/USStatesMap.json"),
                  scales = {'projection': proj, 'color': color_sc},
                  color = case_counts)
fig = bqplot.Figure(marks = [mark], axes = [color_ax])
display(fig)
```

```{code-cell} ipython3
total_cases = states.groupby("date").sum()
```

```{code-cell} ipython3
total_cases["cases"]
```

```{code-cell} ipython3
x_sc = bqplot.DateScale()
y_sc = bqplot.LogScale()

x_ax = bqplot.Axis(scale = x_sc)
y_ax = bqplot.Axis(scale = y_sc, orientation='vertical')

lines = bqplot.Lines(x = total_cases.index, y = total_cases["cases"],
                     scales = {'x': x_sc, 'y': y_sc})

interval_selector = bqplot.interacts.FastIntervalSelector(scale = x_sc)

fig = bqplot.Figure(marks = [lines], axes = [x_ax, y_ax], interaction = interval_selector)
display(fig)
```

```{code-cell} ipython3
interval_selector.selected
```

```{code-cell} ipython3
total_cases.loc[interval_selector.selected[0]:interval_selector.selected[1]]
```

```{code-cell} ipython3

```
