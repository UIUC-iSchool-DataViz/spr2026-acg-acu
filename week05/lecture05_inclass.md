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
title: Lecture05 Inclass
---

```{code-cell} ipython3
import bqplot
import numpy as np
```

```{code-cell} ipython3
bqplot.Figure()
```

```{code-cell} ipython3
x = np.arange(100)
y = np.random.random(100) + 5
```

```{code-cell} ipython3
x_sc = bqplot.LinearScale()
y_sc = bqplot.LinearScale()
```

```{code-cell} ipython3
lines = bqplot.Lines(x = x, y = y, scales = {'x': x_sc, 'y': y_sc})
```

```{code-cell} ipython3
fig = bqplot.Figure(marks = [lines])
display(fig)
```

```{code-cell} ipython3
x_ax = bqplot.Axis(scale = x_sc, label = 'X Value')
```

```{code-cell} ipython3
fig.axes = [x_ax]
```

```{code-cell} ipython3
y_ax = bqplot.Axis(scale = y_sc, label = 'Y Value', orientation = 'vertical')
```

```{code-cell} ipython3
fig.axes.append(y_ax)
```

```{code-cell} ipython3
fig.axes = []
fig.axes = [x_ax, y_ax]
```

```{code-cell} ipython3
lines.colors = ['#ff0000']
```

```{code-cell} ipython3
x = ["The Wild Robot", "Deadpool vs Wolverine", "Beetlejuice Beetlejuice", "Inside Out 2"]
y = [100, 250, 10, 500]
```

```{code-cell} ipython3
y_sc = bqplot.LinearScale()
x_sc = bqplot.OrdinalScale()
```

```{code-cell} ipython3
bar = bqplot.Bars(x = x, y = y, scales = {'x': x_sc, 'y': y_sc})
x_ax = bqplot.Axis(scale = x_sc)
y_ax = bqplot.Axis(scale = y_sc, orientation = 'vertical')
fig = bqplot.Figure(marks=[bar], axes = [x_ax, y_ax])
```

```{code-cell} ipython3
fig
```

```{code-cell} ipython3
selector = bqplot.interacts.IndexSelector(scale = x_sc)
```

```{code-cell} ipython3
fig.interaction = selector
```

```{code-cell} ipython3
selector.selected
```

```{code-cell} ipython3
x = np.mgrid[0.0:4*np.pi:512j]
y = np.sin(x) * np.cos(x) * (0.5 + np.random.random(512))
```

```{code-cell} ipython3
x_sc = bqplot.LinearScale()
y_sc = bqplot.LinearScale()
x_ax = bqplot.Axis(scale = x_sc)
y_ax = bqplot.Axis(scale = y_sc, orientation = 'vertical')
lines = bqplot.Lines(x = x, y = y, scales = {'x': x_sc, 'y': y_sc})
fig = bqplot.Figure(marks = [lines], axes = [x_ax, y_ax])
display(fig)
```

```{code-cell} ipython3
fis = bqplot.interacts.FastIntervalSelector(scale = x_sc, marks = [lines])
fig.interaction = fis
```

```{code-cell} ipython3
fis.selected
```

```{code-cell} ipython3
fis.color = '#0000ff'
```

```{code-cell} ipython3
fis.selected
```

```{code-cell} ipython3
import ipywidgets
import traitlets
```

```{code-cell} ipython3
button = ipywidgets.Button(description = "Regenerate")
```

```{code-cell} ipython3
label = ipywidgets.Label()
```

```{code-cell} ipython3
def convert_selected(value):
    return "%s - %s" % (value[0], value[1])

traitlets.link((fis, 'selected'), (label, 'value'), (convert_selected, None))
```

```{code-cell} ipython3
ipywidgets.VBox([label, fig, button])
```

```{code-cell} ipython3
def regenerate(event):
    y = np.sin(x) * np.cos(x) * (0.5 + np.random.random(512))
    lines.y = y

button.on_click(regenerate)
```

```{code-cell} ipython3
import pandas as pd
```

```{code-cell} ipython3
df = pd.read_csv("building_inventory.csv", 
                na_values = {'Year Acquired': 0,
                             'Year Constructed': 0,
                             'Square Footage': 0})
```

```{code-cell} ipython3
gb = df.groupby(["Year Acquired", "Agency Name"])["Square Footage"].sum()
```

```{code-cell} ipython3
gb
```

```{code-cell} ipython3
gb.loc[:,"Department of Agriculture"]
```

```{code-cell} ipython3
x = gb.loc[:, "Department of Agriculture"].index
y = gb.loc[:, "Department of Agriculture"].values
x_sc = bqplot.LinearScale()
y_sc = bqplot.LinearScale()
x_ax = bqplot.Axis(scale = x_sc)
y_ax = bqplot.Axis(scale = y_sc, orientation = 'vertical')
lines = bqplot.Lines(x = x, y = y, scales = {'x': x_sc, 'y': y_sc})
fig = bqplot.Figure(marks = [lines], axes = [x_ax, y_ax])
display(fig)
```

```{code-cell} ipython3
x = gb[:, "Department of Natural Resources"].index
y = gb[:, "Department of Natural Resources"].values
lines.x = x
lines.y = y
```

```{code-cell} ipython3
select = ipywidgets.Select(options = df["Agency Name"].unique())
```

```{code-cell} ipython3
select
```

```{code-cell} ipython3
select.value
```

```{code-cell} ipython3
def change_y(event):
    new_agency = event['new']
    x = gb[:, new_agency].index
    y = gb[:, new_agency].values
    lines.x = x
    lines.y = y

select.observe(change_y, ["value"])
```

```{code-cell} ipython3
fis = bqplot.interacts.FastIntervalSelector(scale = x_sc, marks = [lines])
fig.interaction = fis
```

```{code-cell} ipython3
fis.color = '#0000ff'
```

```{code-cell} ipython3
label = ipywidgets.Label()
```

```{code-cell} ipython3
def selection_changed(event):
    if event['new'] is None: return
    agency = select.value
    start, stop = event['new']
    total = gb.loc[start:stop, agency].sum()
    label.value = "%s square feet" % (total)
```

```{code-cell} ipython3
fis.unobserve_all()
```

```{code-cell} ipython3
fis.observe(selection_changed, ["selected"])
```

```{code-cell} ipython3
label
```

```{code-cell} ipython3

```
