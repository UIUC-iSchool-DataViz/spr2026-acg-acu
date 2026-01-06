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
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
layout: notebook
title: Fonts a lot bigger
---

# Fonts a lot bigger

```{code-cell} ipython3
import traitlets
```

```{code-cell} ipython3
class MusicAlbum(traitlets.HasTraits):
    name = traitlets.Unicode()
    artist = traitlets.Unicode()
    year = traitlets.Int()
```

```{code-cell} ipython3
t1989 = MusicAlbum(name = "1989 (Taylor's Version)", artist = "Taylor Swift", year = 2023)
```

```{code-cell} ipython3
t1989.name
```

```{code-cell} ipython3
def name_changed(change):
    print("The name has changed from ", change['old'], " to ", change['new'])
t1989.observe(name_changed, ["name"])
```

```{code-cell} ipython3
t1989.name = "1989 (Taylor's Version (Taylor's Version))"
```

```{code-cell} ipython3
t1989.name
```

```{code-cell} ipython3
t1989.name = "1989 (Taylor's Version)"
```

```{code-cell} ipython3
import random
```

```{code-cell} ipython3
class Student(traitlets.HasTraits):
    name = traitlets.Unicode()
    row_and_seat = traitlets.Tuple(
                        traitlets.Unicode(),
                        traitlets.Int()
                    )

    @traitlets.default("row_and_seat")
    def random(self):
        return (random.choice("ABCDEFG"),
                random.randint(1, 15))
```

```{code-cell} ipython3
s1 = Student(name = "Matt")
s2 = Student(name = "Esther")
s3 = Student(name = "Unknown")
```

```{code-cell} ipython3
s1.row_and_seat
```

```{code-cell} ipython3
s2.row_and_seat
```

```{code-cell} ipython3
s3.row_and_seat
```

```{code-cell} ipython3
s4 = Student()
```

```{code-cell} ipython3
traitlets.link( (s1, "name"), (s4, "name") )
```

```{code-cell} ipython3
s4.name
```

```{code-cell} ipython3
s1.name = "Not Matt"
```

```{code-cell} ipython3
s1.name
```

```{code-cell} ipython3
s4.name
```

```{code-cell} ipython3
s4.name = "Matt"
```

```{code-cell} ipython3
s1.name
```

```{code-cell} ipython3
import ipywidgets
```

```{code-cell} ipython3
@ipywidgets.interact( winner = ["Philadelphia", "Kansas City"] )
def say_winner(winner):
    print("The winner was: ", winner)
```

```{code-cell} ipython3
@ipywidgets.interact( winner = ["Philadelphia", "Kansas City"], phil_score = (0, 100), kc_score = (0, 100) )
def say_winner(winner, phil_score, kc_score):
    print("The winner was: ", winner, "with a final score of ", phil_score, "to", kc_score)
```

```{code-cell} ipython3
import matplotlib.pyplot as plt
```

```{code-cell} ipython3
@ipywidgets.interact(style = plt.style.available)
def make_plot(style):
    with plt.style.context(style):
        plt.plot([1,2,3,4], [5,6,7,5])
```

```{code-cell} ipython3
intslider = ipywidgets.IntSlider()
```

```{code-cell} ipython3
intslider
```

```{code-cell} ipython3
intslider.value
```

```{code-cell} ipython3
intslider
```

```{code-cell} ipython3
inttext = ipywidgets.IntText()
```

```{code-cell} ipython3
inttext
```

```{code-cell} ipython3
traitlets.link( ( inttext, "value"), (intslider, "value"))
```

```{code-cell} ipython3
intslider.max = 1000
```

```{code-cell} ipython3
ipywidgets.SelectionSlider(options = ["hi", "option", "choice", "thing"])
```

```{code-cell} ipython3
ta = ipywidgets.Textarea()
```

```{code-cell} ipython3
ta
```

```{code-cell} ipython3
ta
```

```{code-cell} ipython3
ipywidgets.HBox( [
  ipywidgets.Textarea(),
    ipywidgets.VBox([
        ipywidgets.IntSlider(),
        ipywidgets.IntText()
    ])
])
```

```{code-cell} ipython3
ipywidgets.HTML(
    "<table><tr><td>Cell 1</td><td>Cell 2</td></tr><tr><td>Row 2 Cell 1</td><td>Row 2 Cell 2</td></tr></table>"
)
```

```{code-cell} ipython3
html = ipywidgets.HTML()
```

```{code-cell} ipython3
html
```

```{code-cell} ipython3
ta = ipywidgets.Textarea()
```

```{code-cell} ipython3
traitlets.link((ta, "value"), (html, "value"))
```

```{code-cell} ipython3
ta
```

```{code-cell} ipython3
button = ipywidgets.Button(description="Increment")
```

```{code-cell} ipython3
pbar = ipywidgets.IntProgress()
```

```{code-cell} ipython3
def increment_progress(event):
    pbar.value = pbar.value + 1
button.on_click(increment_progress)
```

```{code-cell} ipython3
ipywidgets.HBox([pbar, button])
```

```{code-cell} ipython3
pbar.value
```

```{code-cell} ipython3
pbar.value = 90
```

```{code-cell} ipython3
import time
```

```{code-cell} ipython3
for i in range(101):
    pbar.value = i
    time.sleep(0.1)
```

```{code-cell} ipython3
import bqplot
```

```{code-cell} ipython3
import numpy as np
```

```{code-cell} ipython3
x = np.mgrid[0.0:10.0:256j]
y = np.sin(x)
```

```{code-cell} ipython3
x_sc = bqplot.LinearScale()
y_sc = bqplot.LinearScale()
```

```{code-cell} ipython3
x_ax = bqplot.Axis(scale = x_sc)
y_ax = bqplot.Axis(scale = y_sc, orientation = 'vertical')
```

```{code-cell} ipython3
lines = bqplot.Lines(x = x, y = y, scales = {'x': x_sc, 'y': y_sc})
```

```{code-cell} ipython3
fig = bqplot.Figure(marks = [lines], axes = [x_ax, y_ax])
```

```{code-cell} ipython3
fig
```

```{code-cell} ipython3
tv = ipywidgets.Text()
```

```{code-cell} ipython3
traitlets.link((tv, "value"), (x_ax, "label"))
```

```{code-cell} ipython3
tv
```

```{code-cell} ipython3
lines.y = np.cos(x)
```

```{code-cell} ipython3
fig
```

```{code-cell} ipython3
fis = bqplot.interacts.FastIntervalSelector(scale = x_sc)
```

```{code-cell} ipython3
fig = bqplot.Figure(marks = [lines], axes = [x_ax, y_ax], interaction = fis)
```

```{code-cell} ipython3
fig
```

```{code-cell} ipython3
fis.selected
```

```{code-cell} ipython3
import pandas as pd
```

```{code-cell} ipython3
df = pd.read_csv("building_inventory.csv",
                 na_values = {'Year Acquired': 0, 'Year Constructed': 0},
                 parse_dates = ["Year Acquired", "Year Constructed"])
```

```{code-cell} ipython3
x_sc = bqplot.DateScale()
y_sc = bqplot.LinearScale()
x_ax = bqplot.Axis(scale = x_sc)
y_ax = bqplot.Axis(scale = y_sc, orientation = 'vertical')
points = bqplot.Scatter(x = df["Year Acquired"], y = df["Square Footage"], scales = {'x': x_sc, 'y': y_sc})

fig = bqplot.Figure(marks = [points], axes = [x_ax, y_ax])
x_sc.min = df["Year Acquired"].min()

display(fig)
```

```{code-cell} ipython3
h = ipywidgets.HTML()
display(h)
```

```{code-cell} ipython3
fis = bqplot.interacts.FastIntervalSelector(scale = x_sc)
```

```{code-cell} ipython3
fig.interaction = fis
```

```{code-cell} ipython3
def on_change_selection(change):
    h.value = str(df["Square Footage"][((df["Year Acquired"] > fis.selected[0]) & (df["Year Acquired"] < fis.selected[1]))].sum())
fis.observe(on_change_selection, ["selected"])
```

```{code-cell} ipython3
fis.selected
```

```{code-cell} ipython3
df["Square Footage"][((df["Year Acquired"] > fis.selected[0]) & (df["Year Acquired"] < fis.selected[1]))].sum()
```

```{code-cell} ipython3
fig
```

```{code-cell} ipython3
ipywidgets.HBox([fig, fig])
```

```{code-cell} ipython3
x_sc = bqplot.DateScale()
y_sc = bqplot.LinearScale()
x_ax = bqplot.Axis(scale = x_sc)
y_ax = bqplot.Axis(scale = y_sc, orientation = 'vertical')
points = bqplot.Scatter(x = df["Year Acquired"], y = df["Square Footage"], scales = {'x': x_sc, 'y': y_sc})
pz = bqplot.interacts.PanZoom(scales = {'x': [x_sc], 'y': [y_sc]})
fig = bqplot.Figure(marks = [points], axes = [x_ax, y_ax], interaction = pz)
x_sc.min = df["Year Acquired"].min()

display(fig)
```

```{code-cell} ipython3

```
