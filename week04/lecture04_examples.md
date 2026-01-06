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
title: UNGRADED Workbook for In-Class
---

# UNGRADED Workbook for In-Class

This notebook is here for you to "code along" during class. 

It will not be graded, so feel free to play around!

```{code-cell} ipython3
import ipympl
```

```{code-cell} ipython3
import traitlets
import numpy as np
```

```{code-cell} ipython3
%matplotlib ipympl
```

```{code-cell} ipython3
def something():
    return 2
```

```{code-cell} ipython3
class Album:
    def __init__(self, name, artist):
        self.name = name
        self.artist = artist
```

```{code-cell} ipython3
ttpd = Album("The Tortured Poets' Department", "Taylor Swift")
```

```{code-cell} ipython3
ttpd.name
```

```{code-cell} ipython3
ttpd.artist
```

```{code-cell} ipython3
ttpdtv = Album("The Tortured Poets' Department (Taylor's Version)", "Taylor Swift")
```

```{code-cell} ipython3
ttpdtv.name
```

```{code-cell} ipython3
ttpd.name
```

```{code-cell} ipython3
ttpd.rating = "A++++++"
```

```{code-cell} ipython3
ttpd.rating = 1.5
```

```{code-cell} ipython3
class AlbumCollection:
    def __init__(self, albums):
        self.albums = albums
        
    def average_rating(self):
        rating = 0
        for album in self.albums:
            rating += album.rating
        return rating / len(self.albums)
```

```{code-cell} ipython3
my_coll = AlbumCollection([ttpd, ttpdtv])
```

```{code-cell} ipython3
my_coll.average_rating()
```

```{code-cell} ipython3
import traitlets
```

```{code-cell} ipython3
class MusicAlbum(traitlets.HasTraits):
    name = traitlets.Unicode()
    artist = traitlets.Unicode()
    year_released = traitlets.Int()
```

```{code-cell} ipython3
speak_now = MusicAlbum(name = "Speak Now", artist = "Taylor Swift", year_released = 2010)
```

```{code-cell} ipython3
speak_now.artist
```

```{code-cell} ipython3
speak_now = MusicAlbum(name = "Speak Now", artist = "Taylor Swift", year_released = "2010")
```

```{code-cell} ipython3
class MusicAlbum(traitlets.HasTraits):
    name = traitlets.Unicode()
    artist = traitlets.Unicode()
    year_released = traitlets.CInt()
```

```{code-cell} ipython3
speak_now = MusicAlbum(name = "Speak Now", artist = "Taylor Swift", year_released = "2010")
```

```{code-cell} ipython3
speak_now.year_released
```

```{code-cell} ipython3
class AlbumCollection(traitlets.HasTraits):
    albums = traitlets.List(trait = traitlets.Instance(MusicAlbum))
```

```{code-cell} ipython3
my_collection = AlbumCollection(albums = [speak_now])
```

```{code-cell} ipython3
def name_changed(change):
    print("The name has been changed from '%s' to '%s'" % (change['old'], change['new']))
```

```{code-cell} ipython3
speak_now.observe(name_changed, ['name'])
```

```{code-cell} ipython3
speak_now.name = "Speak Now (Original Version)"
```

```{code-cell} ipython3
red = MusicAlbum(name = "Red", artist = "Taylor Swift", year_released = 2012)
```

```{code-cell} ipython3
red.name = "Red (Original Version)"
```

```{code-cell} ipython3
speak_now.name = "Speak Now (Original Version)"
```

```{code-cell} ipython3
class SomeObject(traitlets.HasTraits):
    name = traitlets.Unicode("Unknown")
    row = traitlets.CInt(1)

```

```{code-cell} ipython3
s = SomeObject()
s.row, s.name
```

```{code-cell} ipython3
import random
```

```{code-cell} ipython3
class SomeObject(traitlets.HasTraits):
    name = traitlets.Unicode("Unknown")
    row = traitlets.CInt(1)

    @traitlets.default("name")
    def _default_name(self):
        return random.choice([
            "Matt", "Other Matt", "Matt Alpha", "Matt One", "Matt Prime", "Zeta Matt"
        ])
```

```{code-cell} ipython3
obj1 = SomeObject()
obj2 = SomeObject()
obj3 = SomeObject()
```

```{code-cell} ipython3
obj1.name, obj2.name, obj3.name
```

```{code-cell} ipython3
import pandas as pd
```

```{code-cell} ipython3
class MyDataFramePlot(traitlets.HasTraits):
    df = traitlets.Instance(pd.DataFrame)
    plotted_x_axis = traitlets.Unicode()
    
    @traitlets.default("plotted_x_axis")
    def _default_plotted_x_axis(self):
        return self.df["Something"].value_count(1)[0]
    
```

```{code-cell} ipython3
class Student(traitlets.HasTraits):
    name = traitlets.Unicode()
    
s1 = Student(name = "Someone's Name")
s2 = Student(name = "")
```

```{code-cell} ipython3
s1.name, s2.name
```

```{code-cell} ipython3
traitlets.link(
    (s1, "name"),
    (s2, "name")
)
```

```{code-cell} ipython3
s2.name
```

```{code-cell} ipython3
s1.name = "My Name"
```

```{code-cell} ipython3
s2.name
```

```{code-cell} ipython3
s2.name = "No, it's my name"
```

```{code-cell} ipython3
s1.name
```

```{code-cell} ipython3
s3 = Student(name = "")
s4 = Student(name = "")

def from_first_to_second(value):
    return "Not actually " + value

def from_second_to_first(value):
    if value.startswith("Not actually "):
        return value[len("Not actually "):]
    else:
        return "Yes actually " + value

traitlets.link(
    (s3, "name"),
    (s4, "name"),
    (from_first_to_second, from_second_to_first)
)
```

```{code-cell} ipython3
s3.name
```

```{code-cell} ipython3
s4.name
```

```{code-cell} ipython3
s4.name = "Not actually Matt"
```

```{code-cell} ipython3
s3.name
```

```{code-cell} ipython3
class KeepsAnInt(traitlets.HasTraits):
    value = traitlets.Int()
    
class KeepsAString(traitlets.HasTraits):
    value = traitlets.Unicode()

```

```{code-cell} ipython3
v1 = KeepsAnInt(value = 0)
v2 = KeepsAString()

traitlets.link((v1, "value"), (v2, "value"), (str, int))
```

```{code-cell} ipython3
v1.value
```

```{code-cell} ipython3
v2.value
```

```{code-cell} ipython3
v2.value = "2024"
```

```{code-cell} ipython3
v1.value
```

```{code-cell} ipython3
import ipywidgets
```

```{code-cell} ipython3
@ipywidgets.interact(name = ['Weezer', 'Nerf Herder', 'Mustard Plug'])
def print_bandname(name):
    print(name)
```

```{code-cell} ipython3
import matplotlib.pyplot as plt
```

```{code-cell} ipython3
@ipywidgets.interact(style = plt.style.available)
def make_plot(style):
    with plt.style.context(style):
        plt.plot([1,2,3,4], [5, 6, 7, 8])
```

```{code-cell} ipython3
@ipywidgets.interact(name = "Name", my_range = (0, 10, 0.1), other = [1, 2, 3, 60], v = False)
def widget_demo(name, my_range, other, v):
    print(name, my_range, other, v)
```

```{code-cell} ipython3
w1 = ipywidgets.BoundedIntText(min = -10, max = 10)
```

```{code-cell} ipython3
w1
```

```{code-cell} ipython3
w1
```

```{code-cell} ipython3
w1.value
```

```{code-cell} ipython3
w2 = ipywidgets.IntSlider(min = -10, max = 10)
traitlets.link((w1, 'value'), (w2, 'value'))
```

```{code-cell} ipython3
w2
```

```{code-cell} ipython3
pb = ipywidgets.IntProgress(min = 0, max=100)
```

```{code-cell} ipython3
pb
```

```{code-cell} ipython3
import time
```

```{code-cell} ipython3
for i in range(101):
    pb.value = i
    time.sleep(0.1)
```

```{code-cell} ipython3
w2.value
```

```{code-cell} ipython3
l = ipywidgets.Label()
```

```{code-cell} ipython3
l
```

```{code-cell} ipython3
l.value = "Hi"
```

```{code-cell} ipython3
traitlets.link(
  (w2, "value"), (l, "value"),
  (str, int)
)
```

```{code-cell} ipython3
import numpy as np
```

```{code-cell} ipython3
@ipywidgets.interact(left_edge = (-10.0, 0.0, 0.1), right_edge = (0.0, 10.0, 0.1), factor = (0.1, 5, 0.01))
def make_plot(left_edge, right_edge, factor):
    x = np.mgrid[left_edge:right_edge:100j]
    y = np.sin(factor * x)
    plt.plot(x, y)
```

```{code-cell} ipython3
ipywidgets.ToggleButtons(options = ["Hi", "There", "Folks"])
```

```{code-cell} ipython3
ipywidgets.Checkbox(description = "Should we?")
```

```{code-cell} ipython3
ipywidgets.Textarea(value = "Write your text here", description = "What are you going to do today?")
```

```{code-cell} ipython3
w2
```

```{code-cell} ipython3
w2.orientation = 'vertical'
```

```{code-cell} ipython3
w2.description = "Something"
```

```{code-cell} ipython3
w2.min = -10
```

```{code-cell} ipython3
dd = ipywidgets.Dropdown(
  options = [("Red", "#ff0000"), ("Green", "#00ff00"), ("Blue", "#0000ff")]
)
```

```{code-cell} ipython3
dd
```

```{code-cell} ipython3
dd.value
```

```{code-cell} ipython3
sm = ipywidgets.SelectMultiple(options = ["Red", "Green", "Blue"])
sm
```

```{code-cell} ipython3
sm.value
```

```{code-cell} ipython3
ipywidgets.RadioButtons(options = ["Red", "Green", "Blue"])
```

```{code-cell} ipython3
ipywidgets.HBox([
    w2, dd, sm
])
```

```{code-cell} ipython3
ipywidgets.VBox([
    w2, dd, sm
])
```

```{code-cell} ipython3
ipywidgets.HBox([
    ipywidgets.VBox([
        dd, sm
    ]),
    w2,
])
```

```{code-cell} ipython3
t = ipywidgets.Tab(
  [dd, w2, sm]
)
t.set_title(0, "dd")
t.set_title(1, "w2")
t.set_title(2, "sm")
```

```{code-cell} ipython3
t
```

```{code-cell} ipython3
cp = ipywidgets.ColorPicker()
```

```{code-cell} ipython3
cp
```

```{code-cell} ipython3
cp.value
```

```{code-cell} ipython3
cp.disabled = False
```

```{code-cell} ipython3
ipywidgets.FileUpload()
```

```{code-cell} ipython3
d = ipywidgets.DatePicker()
```

```{code-cell} ipython3
d
```

```{code-cell} ipython3
d.value
```

```{code-cell} ipython3
dt = ipywidgets.DatePicker()
```

```{code-cell} ipython3
dt
```

```{code-cell} ipython3
val = open("winter_scene.png", "rb").read()
```

```{code-cell} ipython3
im = ipywidgets.Image(value = val)
```

```{code-cell} ipython3
im
```

```{code-cell} ipython3
im.value = open("stitch_reworked.png", "rb").read()
```

```{code-cell} ipython3
f = ipywidgets.FileUpload()
```

```{code-cell} ipython3
f
```

```{code-cell} ipython3
im.value = f.value['winter_scene.png']['content']
```

```{code-cell} ipython3
x = np.mgrid[0:1000000]
y = np.sin(x) * 100
```

```{code-cell} ipython3
import IPython.display
```

```{code-cell} ipython3
IPython.display.Markdown(r"""
# This is a markdown

All my stuff goes in here

""")
```

```{code-cell} ipython3
IPython.display.HTML("<b>Hi!</b>")
```

```{code-cell} ipython3
output = ipywidgets.Output()
```

```{code-cell} ipython3
display(output)
```

```{code-cell} ipython3
output.clear_output()
```

```{code-cell} ipython3
b = ipywidgets.Button(description = "Hi")
```

```{code-cell} ipython3
b
```

```{code-cell} ipython3
b.button_style="info"
```

```{code-cell} ipython3
b.on_click
```

```{code-cell} ipython3
def clicked(event):
    print("Clicked!")
```

```{code-cell} ipython3
b.on_click(clicked)
```

```{code-cell} ipython3
class RandomNumberPlot(traitlets.HasTraits):
    center = traitlets.Float(0.0)
    width = traitlets.Float(10.0)
    color = traitlets.Unicode("#ff0000")
    size = traitlets.Int(256, min=1, max=256*256)
    x = traitlets.Instance(np.ndarray)
    y = traitlets.Instance(np.ndarray)
    
    @traitlets.default("x")
    def random_series_x(self):
        return np.random.normal(self.center, self.width, self.size)
    
    @traitlets.default("y")
    def random_series_y(self):
        return np.random.normal(self.center, self.width, self.size)
    
    def _ipython_display_(self):
        center = ipywidgets.FloatSlider(description = "Center")
        traitlets.link((self, 'center'), (center, 'value'))
        width = ipywidgets.FloatSlider(description = "Width")
        traitlets.link((self, 'width'), (width, "value"))
        
        size = ipywidgets.IntSlider(description = "Size",
                                    min = 1, max=256*256)
        traitlets.link((self, 'size'), (size, 'value'))
        
        color = ipywidgets.ColorPicker(description = "color")
        traitlets.link((self, 'color'), (color, 'value'))
        
        replot = ipywidgets.Button(description = "Replot")
        
        plot_output = ipywidgets.Output()
        def update_plot(event):
            self.x = self.random_series_x()
            self.y = self.random_series_y()
            plot_output.clear_output()
            with plot_output:
                fig, ax = plt.subplots()
                ax.scatter(self.x, self.y, color = self.color, s = 0.1)
        replot.on_click(update_plot)
        im = ipywidgets.Image(height = 300, width=300)
        display(
            ipywidgets.HBox([
                ipywidgets.VBox([center, width, size, color, replot], layout = {'border': '1px solid green',
                                                                                'align_items': 'center'}),
                plot_output
            ], layout = {'border': '1px solid black'})
        )
```

```{code-cell} ipython3
rnp = RandomNumberPlot()
```

```{code-cell} ipython3
rnp
```

```{code-cell} ipython3
a = ipywidgets.VBox()
```

```{code-cell} ipython3
a.layout.traits()
```

```{code-cell} ipython3

```
