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
title: Week04-Inclass-02
---

```{code-cell} ipython3
import traitlets
import ipywidgets
```

```{code-cell} ipython3
a = ipywidgets.IntSlider()
b = ipywidgets.IntText()
traitlets.link((a, 'value'), (b, 'value'))
```

```{code-cell} ipython3
a
```

```{code-cell} ipython3
b
```

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt
```

```{code-cell} ipython3
np.mgrid[0.0:10.0:0.5]
```

```{code-cell} ipython3
np.mgrid[0.0:1.0:4j]
```

```{code-cell} ipython3
np.mgrid[0.0:10.0:256j]
```

```{code-cell} ipython3
x = np.mgrid[0.0:10.0:256j]
y = np.sin(1 * x)
```

```{code-cell} ipython3
plt.plot(x, y)
```

```{code-cell} ipython3
@ipywidgets.interact( factor = ( 0.0, 2.5, 0.1) )
def make_plot(factor):
    x = np.mgrid[0.0:10.0:256j]
    y = np.sin(factor * x)
    plt.plot(x, y)
```

```{code-cell} ipython3
fw = ipywidgets.FloatText()
```

```{code-cell} ipython3
@ipywidgets.interact( factor = fw, color = ipywidgets.ColorPicker(), file = ipywidgets.FileUpload() )
def make_plot(factor, color):
    x = np.mgrid[0.0:10.0:256j]
    y = np.sin(factor * x)
    plt.plot(x, y, c = color)
```

```{code-cell} ipython3
fw.value = 9.5
```

```{code-cell} ipython3
ipywidgets.ColorPicker()
```

```{code-cell} ipython3
fup = ipywidgets.FileUpload()
```

```{code-cell} ipython3
fup
```

```{code-cell} ipython3
fup.value
```

```{code-cell} ipython3
dp = ipywidgets.DatePicker()
```

```{code-cell} ipython3
dp
```

```{code-cell} ipython3
dp.value
```

```{code-cell} ipython3
hb = ipywidgets.HBox([ ipywidgets.FileUpload(), ipywidgets.IntSlider() ])
```

```{code-cell} ipython3
hb
```

```{code-cell} ipython3
hb.layout.border = '1px solid black'
```

```{code-cell} ipython3
class SimpleTraitlets(traitlets.HasTraits):
    my_name = traitlets.Unicode()
```

```{code-cell} ipython3
st = SimpleTraitlets(name = "Hi")
```

```{code-cell} ipython3
st.traits()
```

```{code-cell} ipython3
hb.layout.traits()
```

```{code-cell} ipython3
hb.layout.justify_content = 'center'
```

```{code-cell} ipython3
hb
```

```{code-cell} ipython3
fw.value = 10
```

```{code-cell} ipython3
class MySineGraph(traitlets.HasTraits):
    offset = traitlets.Float()
    factor = traitlets.Float()

    def _ipython_display_(self):
        x = np.mgrid[0.0:10.0:256j]
        y = np.sin(x*self.factor + self.offset)
        plt.plot(x, y)
```

```{code-cell} ipython3
import io
```

```{code-cell} ipython3
b = io.BytesIO()
plt.savefig(b)
```

```{code-cell} ipython3
b.seek(0)
ipywidgets.Image(value = b.read())
```

```{code-cell} ipython3
msg = MySineGraph(offset = 0.0, factor = 2.0)
```

```{code-cell} ipython3
msg
```

```{code-cell} ipython3
class MySineGraph(traitlets.HasTraits):
    offset = traitlets.Float()
    factor = traitlets.Float()
    image = traitlets.Bytes()

    def make_plot(self):
        x = np.mgrid[0.0:10.0:256j]
        y = np.sin(x*self.factor + self.offset)
        plt.plot(x, y)
        b = io.BytesIO()
        plt.savefig(b)
        b.seek(0)
        self.image = b.read()
    
    def _ipython_display_(self):
        im = ipywidgets.Image()
        traitlets.link((self, 'image'), (im, 'value'))
        display(im)
```

```{code-cell} ipython3
msg = MySineGraph()
```

```{code-cell} ipython3
msg
```

```{code-cell} ipython3
msg.make_plot()
```

```{code-cell} ipython3
class MySineGraph(traitlets.HasTraits):
    offset = traitlets.Float()
    factor = traitlets.Float()
    image = traitlets.Bytes()

    @traitlets.observe('factor', 'offset')
    def _plot_changed(self, change):
        x = np.mgrid[0.0:10.0:256j]
        y = np.sin(x*self.factor + self.offset)
        plt.clf()
        plt.plot(x, y)
        b = io.BytesIO()
        plt.savefig(b)
        b.seek(0)
        self.image = b.read()
    
    def _ipython_display_(self):
        im = ipywidgets.Image()
        traitlets.link((self, 'image'), (im, 'value'))
        display(im)
```

```{code-cell} ipython3
msg = MySineGraph(factor = 1.0, offset = 0.0)
```

```{code-cell} ipython3
msg
```

```{code-cell} ipython3
msg.factor = 2.0
```

```{code-cell} ipython3
msg.factor = 2.0
```

```{code-cell} ipython3
import bqplot
```

```{code-cell} ipython3

```

```{code-cell} ipython3
class MySineGraph(traitlets.HasTraits):
    factor = traitlets.Float()
    offset = traitlets.Float()
    n = traitlets.Int(256)
    figure = traitlets.Instance(bqplot.Figure)

    @traitlets.default("figure")
    def _default_figure(self):
        x_sc = bqplot.LinearScale()
        y_sc = bqplot.LinearScale()
        x_ax = bqplot.Axis(scale = x_sc)
        y_ax = bqplot.Axis(scale = y_sc, orientation = 'vertical')

        mark = bqplot.Lines(x = [], y = [], scales = {'x': x_sc, 'y': y_sc})
        fig = bqplot.Figure(marks = [mark], axes = [x_ax, y_ax])
        return fig

    @traitlets.observe("factor", "offset", "n")
    def _change_factor_offset(self, change):
        x = np.mgrid[0.0:10.0:1j * self.n]
        y = np.sin(self.factor * x + self.offset)
        self.figure.marks[0].x = x
        self.figure.marks[0].y = y
    
    def _ipython_display_(self):
        display(self.figure)
```

```{code-cell} ipython3
msg = MySineGraph(factor = 1.0, offset = 0.0)
```

```{code-cell} ipython3
msg
```

```{code-cell} ipython3
msg.factor = 4
```

```{code-cell} ipython3
fs = ipywidgets.FloatSlider()
traitlets.link((fs, 'value'), (msg, 'factor'))
fs
```

```{code-cell} ipython3
ns = ipywidgets.IntSlider(min = 1, max = 2048)
traitlets.link((ns, 'value'), (msg, 'n'))
ns
```

```{code-cell} ipython3

```
