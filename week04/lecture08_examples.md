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
  display_name: Environment (conda_conda)
  language: python
  name: conda_conda
layout: notebook
title: Lecture08 Examples
---

```{code-cell} ipython3
import bqplot
import numpy as np
import ipywidgets
import traitlets
```

```{code-cell} ipython3
x = np.arange(100)
```

```{code-cell} ipython3
x
```

```{code-cell} ipython3
x.ndim, x.shape, x.dtype
```

```{code-cell} ipython3
y = np.random.random(100) + 5
```

```{code-cell} ipython3
x_sc = bqplot.LinearScale()
y_sc = bqplot.LinearScale()
```

```{code-cell} ipython3
x_sc.traits()
```

```{code-cell} ipython3
lines = bqplot.Lines(x = x, y = y, scales = {'x': x_sc, 'y': y_sc})

x_ax = bqplot.Axis(scale = x_sc, label = "X Axis")
y_ax = bqplot.Axis(scale = y_sc, label = "Y Axis", orientation = "vertical")

fig = bqplot.Figure(marks = [lines], axes = [x_ax, y_ax])

display(fig)
```

```{code-cell} ipython3
y_lower_bound = ipywidgets.FloatSlider(min = 0, max = 10)
y_upper_bound = ipywidgets.FloatSlider(min = 0, max = 10)
traitlets.link((y_lower_bound, 'value'), (y_sc, 'min'))
traitlets.link((y_upper_bound, 'value'), (y_sc, 'max'))

regenerate_button = ipywidgets.Button(description="Regenerate!")

def regenerate_y(button):
    mi_val = y_sc.min
    ma_val = y_sc.max
    lines.y = np.random.random(100) * (ma_val - mi_val) + mi_val

regenerate_button.on_click(regenerate_y)

display(ipywidgets.VBox([regenerate_button, y_upper_bound, y_lower_bound, fig]))
```

```{code-cell} ipython3
label1 = ipywidgets.Text("label 1", disabled = True)
label2 = ipywidgets.Text("label 2", disabled = True)
vbox = ipywidgets.VBox([label1, label2])
display(vbox)
```

```{code-cell} ipython3
x = np.arange(100)
y0 = np.random.random(100) * 5.0
y1 = np.random.random(100) + 2.0

x_sc = bqplot.LinearScale()
y_sc = bqplot.LinearScale()

lines = bqplot.Lines(x = x, y = [y0, y1], scales = {'x': x_sc, 'y': y_sc})

x_ax = bqplot.Axis(scale = x_sc, label = "X Axis")
y_ax = bqplot.Axis(scale = y_sc, label = "Y Axis", orientation = "vertical")

fig = bqplot.Figure(marks = [lines], axes = [x_ax, y_ax])

display(fig)
```

```{code-cell} ipython3
x = np.arange(100)
y0 = np.random.random(100) * 5.0
y1 = np.random.random(100) + 2.0

x_sc = bqplot.LinearScale()
y_sc = bqplot.LinearScale()

lines = bqplot.Lines(x = x, y = [y0, y1], scales = {'x': x_sc, 'y': y_sc})
points = bqplot.Scatter(x = x, y = y0, scales = {'x': x_sc, 'y': y_sc})

x_ax = bqplot.Axis(scale = x_sc, label = "X Axis")
y_ax = bqplot.Axis(scale = y_sc, label = "Y Axis", orientation = "vertical")

fig = bqplot.Figure(marks = [lines, points], axes = [x_ax, y_ax])

display(fig)
```

```{code-cell} ipython3
x = np.arange(100)
y0 = np.random.random(100) * 5.0
y1 = np.random.random(100) + 2.0

x_sc = bqplot.LinearScale()
y_sc = bqplot.LinearScale()

lines = bqplot.Lines(x = x, y = [y0, y1], scales = {'x': x_sc, 'y': y_sc})
points = bqplot.Scatter(x = x, y = y0, scales = {'x': x_sc, 'y': y_sc})

x_ax = bqplot.Axis(scale = x_sc, label = "X Axis")
y_ax = bqplot.Axis(scale = y_sc, label = "Y Axis", orientation = "vertical")

pan_zoom = bqplot.PanZoom(scales = {'x': [x_sc], 'y': [y_sc]})

fig = bqplot.Figure(marks = [lines, points], axes = [x_ax, y_ax], interaction = pan_zoom)

display(fig)
```

```{code-cell} ipython3

```
