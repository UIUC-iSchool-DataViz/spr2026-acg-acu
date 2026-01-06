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
title: Lecture13 Examples
---

```{code-cell} ipython3
import pandas as pd
import numpy as np
```

```{code-cell} ipython3
df = pd.read_csv("building_inventory.csv", na_values = {
    "Year Acquired": 0,
    "Year Constructed": 0,
    "Square Footage": 0
})
```

```{code-cell} ipython3
df["Year Acquired"] = pd.to_datetime(df["Year Acquired"], format = "%Y")
df["Year Constructed"] = pd.to_datetime(df["Year Constructed"], format = "%Y")
```

```{code-cell} ipython3
y_a = df["Year Acquired"]
```

```{code-cell} ipython3
df.groupby("Year Acquired")["Square Footage"].sum().plot()
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
states.dtypes
```

```{code-cell} ipython3
states["state"] == "Washington"
```

```{code-cell} ipython3
states[states["state"] == "Washington"]
```

```{code-cell} ipython3
pd.to_datetime(states["date"])
```

```{code-cell} ipython3
illinois_results = states[states["state"] == "Illinois"]
```

```{code-cell} ipython3
import bqplot
```

```{code-cell} ipython3
x_sc = bqplot.DateScale()
y_sc = bqplot.LinearScale()

x_ax = bqplot.Axis(scale = x_sc, label = "Date")
y_ax = bqplot.Axis(scale = y_sc, orientation = 'vertical', label = "Cases (cumulative)")

lines = bqplot.Lines(x = illinois_results["date"], y = illinois_results["cases"],
                     scales = {'x': x_sc, 'y': y_sc})

fig = bqplot.Figure(marks = [lines], axes = [x_ax, y_ax])
display(fig)
```

```{code-cell} ipython3
x_sc = bqplot.DateScale()
y_sc = bqplot.LinearScale()

x_ax = bqplot.Axis(scale = x_sc, label = "Date")
y_ax = bqplot.Axis(scale = y_sc, orientation = 'vertical', label = "Cases (cumulative)")

lines = bqplot.Lines(x = illinois_results["date"], y = illinois_results["cases"],
                     scales = {'x': x_sc, 'y': y_sc})

date_selection = bqplot.interacts.FastIntervalSelector(scale = x_sc)

fig = bqplot.Figure(marks = [lines], axes = [x_ax, y_ax], interaction = date_selection)
display(fig)
```

```{code-cell} ipython3
states
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
#color_sc = bqplot.ColorScale(colors = ["white", "black"])
color_sc = bqplot.ColorScale(scheme = "viridis")
color_ax = bqplot.ColorAxis(scale = color_sc, label = 'Case Count')

mark = bqplot.Map(map_data = bqplot.topo_load("map_data/USStatesMap.json"),
                  scales = {'projection': proj, 'color': color_sc},
                  color = case_counts)
fig = bqplot.Figure(marks = [mark], axes = [color_ax])
display(fig)
```

```{code-cell} ipython3
counties = pd.read_csv("us-counties.csv", parse_dates = ["date"],
                       dtype = {'fips': pd.Int32Dtype()})
```

```{code-cell} ipython3
illinois_by_county = counties[counties["state"] == "Illinois"]
```

```{code-cell} ipython3
case_counts = illinois_by_county.groupby("fips")["cases"].max().to_dict()

proj = bqplot.AlbersUSA()
color_sc = bqplot.ColorScale(scheme = "BuPu")
color_ax = bqplot.ColorAxis(scale = color_sc, label = 'Case Count')

mark = bqplot.Map(map_data = bqplot.topo_load("map_data/USCountiesMap.json"),
                  scales = {'projection': proj, 'color': color_sc},
                  color = case_counts)
fig = bqplot.Figure(marks = [mark], axes = [color_ax])
display(fig)
```

```{code-cell} ipython3
import ipywidgets
v = ipywidgets.Label()
display(v)
```

```{code-cell} ipython3
def hover_over_county(name, value):
    v.value = "%s" % (value)
```

```{code-cell} ipython3
mark.on_hover(hover_over_county)
```

```{code-cell} ipython3

```
