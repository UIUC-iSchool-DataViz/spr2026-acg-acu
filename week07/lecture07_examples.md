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
  display_name: py311
  language: python
  name: py311
layout: notebook
title: Lecture07 Examples
---

```{code-cell} ipython3
import pandas as pd
```

```{code-cell} ipython3
counties = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv",
                       parse_dates = ["date"])
```

```{code-cell} ipython3
states = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv",
                    parse_dates = ["date"])
```

```{code-cell} ipython3
states
```

```{code-cell} ipython3
states.dtypes
```

```{code-cell} ipython3
counties
```

```{code-cell} ipython3
counties.dtypes

illinois_results = states[
    states["state"] == "Illinois"
]
```

```{code-cell} ipython3
illinois_results
```

```{code-cell} ipython3
illinois_results["date"] == "January 28, 2020"
```

```{code-cell} ipython3
import bqplot
```

```{code-cell} ipython3
x_sc = bqplot.DateScale()
y_sc = bqplot.LinearScale()

x_ax = bqplot.Axis(scale = x_sc, label = "Date")
y_ax = bqplot.Axis(scale = y_sc, label = "Cases (cumulative)", orientation = "vertical")

lines = bqplot.Lines(x = illinois_results["date"], y = illinois_results["cases"],
                    scales = {'x': x_sc, 'y': y_sc})

fig = bqplot.Figure(marks = [lines], axes = [x_ax, y_ax])
display(fig)
```

```{code-cell} ipython3
x_sc = bqplot.DateScale()
y_sc = bqplot.LinearScale()

x_ax = bqplot.Axis(scale = x_sc, label = "Date")
y_ax = bqplot.Axis(scale = y_sc, label = "Cases (cumulative)", orientation = "vertical")

lines = bqplot.Lines(x = illinois_results["date"], y = illinois_results["cases"],
                    scales = {'x': x_sc, 'y': y_sc})

date_selection = bqplot.interacts.FastIntervalSelector(scale = x_sc)

fig = bqplot.Figure(marks = [lines], axes = [x_ax, y_ax], interaction = date_selection)
display(fig)
```

```{code-cell} ipython3
date_selection.selected
```

```{code-cell} ipython3
import ipywidgets
```

```{code-cell} ipython3
label = ipywidgets.Label()
display(label)
```

```{code-cell} ipython3
def watch_selection(change):
    selected_range = illinois_results.loc[change['new'][0] : change['new'][1]]
    delta_cases = selected_range["cases"].max() - selected_range["cases"].min()
    label.value = "An increase of %s" % delta_cases
date_selection.unobserve_all()
date_selection.observe(watch_selection, ["selected"])
```

```{code-cell} ipython3
illinois_results.set_index("date", inplace=True)
illinois_results.loc[date_selection.selected[0] : date_selection.selected[1]]
```

```{code-cell} ipython3
in_range = ((illinois_results["date"] < date_selection.selected[1])
          & (illinois_results["date"] > date_selection.selected[0]))
```

```{code-cell} ipython3
illinois_results[in_range]["cases"]
```

```{code-cell} ipython3
illinois_results = states[
    states["state"] == "Illinois"
]
```

```{code-cell} ipython3
illinois_results.set_index("date", inplace=True)
```

```{code-cell} ipython3
illinois_results
```

```{code-cell} ipython3
state_map = bqplot.topo_load("map_data/USStatesMap.json")
```

```{code-cell} ipython3
cases_by_fips = states.groupby("fips")["cases"].max().to_dict()
```

```{code-cell} ipython3
proj = bqplot.AlbersUSA()
color_sc = bqplot.ColorScale(scheme = "BuPu")
color_ax = bqplot.ColorAxis(scale = color_sc)
map_mark = bqplot.Map(map_data = state_map, color = cases_by_fips,
                      scales = {'projection': proj,
                               'color': color_sc}
)
fig = bqplot.Figure(marks = [map_mark], axes = [color_ax])
display(fig)
```

```{code-cell} ipython3
label2 = ipywidgets.Label()
display(label2)
```

```{code-cell} ipython3
def hover_over_state(mark, hover_info):
    label2.value = "%s had %s cases" % (hover_info['data']['name'], hover_info['data']['color'])
map_mark.on_hover(hover_over_state)
```

```{code-cell} ipython3
bqplot.__version__
```

```{code-cell} ipython3
ipywidgets.VBox([
    label2,
    fig,
])
```

```{code-cell} ipython3
x_sc = bqplot.DateScale()
y_sc = bqplot.LinearScale()

x_ax = bqplot.Axis(scale = x_sc, label = "Date")
y_ax = bqplot.Axis(scale = y_sc, label = "Cases (cumulative)", orientation = "vertical")

lines = bqplot.Lines(x = illinois_results.index, y = illinois_results["cases"],
                    scales = {'x': x_sc, 'y': y_sc})

date_selection = bqplot.interacts.FastIntervalSelector(scale = x_sc)

line_fig = bqplot.Figure(marks = [lines], axes = [x_ax, y_ax], interaction = date_selection)

proj = bqplot.AlbersUSA()
color_sc = bqplot.ColorScale(scheme = "BuPu")
color_ax = bqplot.ColorAxis(scale = color_sc)
map_mark = bqplot.Map(map_data = state_map, color = cases_by_fips,
                      scales = {'projection': proj,
                               'color': color_sc}
)
map_fig = bqplot.Figure(marks = [map_mark], axes = [color_ax])

ipywidgets.VBox([
    line_fig,
    map_fig
])
```

```{code-cell} ipython3
line_fig.layout.height = "250px"
map_fig.layout.height = "400px"
```

```{code-cell} ipython3
states_by_date = states.set_index("date")
```

```{code-cell} ipython3
def change_date_selection(change):
    max_cases = states_by_date.loc[change['new'][0]:change['new'][1]].groupby("fips")["cases"].max().to_dict()
    print(max_cases)
    map_mark.color = max_cases
date_selection.unobserve_all()
date_selection.observe(change_date_selection, ["selected"])
```

```{code-cell} ipython3
states_by_date.loc[date_selection.selected[0] : date_selection.selected[1]].groupby("fips")["cases"].max().to_dict()
```

```{code-cell} ipython3

map_mark.color
```

```{code-cell} ipython3

```
