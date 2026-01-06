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
title: Lecture07 Examples
---

```{code-cell} ipython3
import traitlets
import ipywidgets
```

```{code-cell} ipython3
class Band(traitlets.HasTraits):
    name = traitlets.Unicode()
    age = traitlets.Int()
```

```{code-cell} ipython3
weezer = Band(name = "Weezer", age = 26)
```

```{code-cell} ipython3
weezer.name
```

```{code-cell} ipython3
weezer.age
```

```{code-cell} ipython3
weezer.name
```

```{code-cell} ipython3
def name_changed(change):
    print("Band name has changed from {} to {}".format(
        change['old'], change['new']))
```

```{code-cell} ipython3
weezer.observe(name_changed, ['name'])
```

```{code-cell} ipython3
weezer.name
```

```{code-cell} ipython3
weezer.name = "White Stripes"
```

```{code-cell} ipython3
weezer.unobserve_all()
```

```{code-cell} ipython3
def trait_changed(change):
    print("The trait {name} has changed from {old} to {new}".format(
        **change))
```

```{code-cell} ipython3
weezer = Band(name = "Weezer", age = 26)
weezer.observe(trait_changed, ['name', 'age'])
```

```{code-cell} ipython3
weezer.age = 10
```

```{code-cell} ipython3
weezer.name = "Something Else"
```

```{code-cell} ipython3
weezer.name = "Something Else"
```

```{code-cell} ipython3
class Record(traitlets.HasTraits):
    band_name = traitlets.Unicode()
```

```{code-cell} ipython3
some_record = Record(band_name = "")
```

```{code-cell} ipython3
traitlets.link( (weezer, 'name'), (some_record, 'band_name') )
```

```{code-cell} ipython3
some_record.band_name
```

```{code-cell} ipython3
weezer.name = "Weezer"
```

```{code-cell} ipython3
some_record.band_name
```

```{code-cell} ipython3
some_record.band_name = "TMBG"
```

```{code-cell} ipython3
@ipywidgets.interact(name = ['Weezer', 'Nerf Herder', 'Mustard Plug'],
                    age = (0, 100, 5),
                    message = "hi")
def print_bandname(name = "Mustard Plug", age = 10, message = "hi"):
    print(name, age, message)
```

```{code-cell} ipython3
fs = ipywidgets.FloatSlider()
```

```{code-cell} ipython3
display(fs)
```

```{code-cell} ipython3
fs.max = 50
```

```{code-cell} ipython3
fs.min = 10.
```

```{code-cell} ipython3
display(fs)
```

```{code-cell} ipython3
fs.value
```

```{code-cell} ipython3
def print_value(change):
    print("Trait changed from {old} to {new}".format(**change))
fs.observe(print_value, ['value'])
```

```{code-cell} ipython3
fs.unobserve_all()
```

```{code-cell} ipython3
ipywidgets.IntRangeSlider()
```

```{code-cell} ipython3
log_slider = ipywidgets.FloatLogSlider()
```

```{code-cell} ipython3
display(log_slider)
```

```{code-cell} ipython3
log_slider.value = 1e3
```

```{code-cell} ipython3
pbar = ipywidgets.FloatProgress()
```

```{code-cell} ipython3
display(pbar)
```

```{code-cell} ipython3
import time
```

```{code-cell} ipython3
for i in range(100):
    pbar.value = i
    time.sleep(0.1)
```

```{code-cell} ipython3
bft = ipywidgets.BoundedFloatText(min = 25.0, max = 53.0, value = 25.1)
```

```{code-cell} ipython3
bft
```

```{code-cell} ipython3
traitlets.link((bft, 'value'), (log_slider, 'value'))
```

```{code-cell} ipython3
my_display = ipywidgets.HTML()
```

```{code-cell} ipython3
my_display
```

```{code-cell} ipython3
my_display.value = "hi there <b>this is bold</b>"
```

```{code-cell} ipython3
text_entry = ipywidgets.Textarea()
text_display = ipywidgets.HTML()

traitlets.link( (text_entry, "value"), (text_display, "value") )
```

```{code-cell} ipython3
display(text_entry)
```

```{code-cell} ipython3
display(text_display)
```

```{code-cell} ipython3
ipywidgets.HBox([text_entry, text_display])
```

```{code-cell} ipython3
ipywidgets.VBox([text_entry, text_display])
```

```{code-cell} ipython3
ipywidgets.HBox([
    ipywidgets.VBox([text_entry, text_display]),
    ipywidgets.IntSlider()
])
```

```{code-cell} ipython3
slider = ipywidgets.SelectionSlider(options = ["Weezer", "Nerf Herder", "Mustard Plug"])
```

```{code-cell} ipython3
slider
```

```{code-cell} ipython3
slider.index
```

```{code-cell} ipython3
slider.value
```

```{code-cell} ipython3
rb = ipywidgets.RadioButtons(options = ["This", "That", "The Other"])
display(rb)
```

```{code-cell} ipython3
rb.index
```

```{code-cell} ipython3
rb.value
```

```{code-cell} ipython3
ipywidgets.Checkbox(description="Enabled")
```

```{code-cell} ipython3
@ipywidgets.interact(message = ipywidgets.Textarea())
def print_message(message):
    print(message)
```

```{code-cell} ipython3
button = ipywidgets.Button(description = "Does Something")
display(button)
```

```{code-cell} ipython3
def button_clicked(obj):
    print(obj)
button.on_click(button_clicked)
```

```{code-cell} ipython3
class SomeRandomValue(traitlets.HasTraits):
    value1 = traitlets.Float()
    value2 = traitlets.Float()
srv = SomeRandomValue()
```

```{code-cell} ipython3
button1 = ipywidgets.Button(description = "Change value1")
button2 = ipywidgets.Button(description = "Change value2")
```

```{code-cell} ipython3
value1_floatslider = ipywidgets.FloatSlider()
value2_floatslider = ipywidgets.FloatSlider()
```

```{code-cell} ipython3
ipywidgets.HBox([
    ipywidgets.VBox([button1, button2]),
    ipywidgets.VBox([value1_floatslider, value2_floatslider])
])
```

```{code-cell} ipython3
import random
```

```{code-cell} ipython3
def change_value1(button):
    srv.value1 = random.randrange(0.0, 100.0)
def change_value2(button):
    srv.value2 = random.randrange(0.0, 100.0)
```

```{code-cell} ipython3
srv.value1, srv.value2
```

```{code-cell} ipython3
button1.on_click(change_value1)
button2.on_click(change_value2)
```

```{code-cell} ipython3
srv.value1
```

```{code-cell} ipython3
srv.value2
```

```{code-cell} ipython3
traitlets.link( (value1_floatslider, 'value'), (srv, 'value1') )
traitlets.link( (value2_floatslider, 'value'), (srv, 'value2') )
```

```{code-cell} ipython3
ipywidgets.ColorPicker()
```

```{code-cell} ipython3
ipywidgets.Controller()
```

```{code-cell} ipython3
ipywidgets.Video()
```

```{code-cell} ipython3
ipywidgets.Play()
```

```{code-cell} ipython3
%matplotlib inline
```

```{code-cell} ipython3
import matplotlib.pyplot as plt
```

```{code-cell} ipython3
import numpy as np
```

```{code-cell} ipython3
x = np.random.random(size = 10000)
y = np.random.normal(size = 10000)
```

```{code-cell} ipython3
@ipywidgets.interact(n = (10, 1000))
def make_plot(n = 100):
    plt.scatter(x[:n], y[:n])
```

```{code-cell} ipython3
import h5py
f = h5py.File("single_dicom.h5", mode = "r")
scan = f["scan"][:]
```

```{code-cell} ipython3
fig, ax = plt.subplots(2,2, dpi = 150)

@ipywidgets.interact( x_ind = (0, scan.shape[0]),
                      y_ind = (0, scan.shape[1]),
                      z_ind = (0, scan.shape[2]))
def sliceit(x_ind = 18, y_ind = 256, z_ind = 256):
    ax[0,0].imshow(scan[x_ind,:,:], extent = [0.0, 1.0, 0.0, 1.0])
    ax[1,0].imshow(scan[:,y_ind,:], extent = [0.0, 1.0, 0.0, 1.0])
    ax[0,1].imshow(scan[:,:,z_ind], extent = [0.0, 1.0, 0.0, 1.0])
    ax[1,1].clear()
    return fig
```

```{code-cell} ipython3

```
