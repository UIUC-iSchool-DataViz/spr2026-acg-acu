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
title: Ipywidgets Intro
---

```{code-cell} ipython3
import traitlets
```

```{code-cell} ipython3
class MusicAlbum:
    pass

simple_album = MusicAlbum()
simple_album.year_released = 2010
simple_album.artist = "Taylor Swift"
simple_album.name = "Speak Now"
```

```{code-cell} ipython3
simple_album.year_released = "fourteen years ago"
```

```{code-cell} ipython3
simple_album.year_released
```

```{code-cell} ipython3
class MusicAlbum(traitlets.HasTraits):
    year_released = traitlets.Int()
    artist = traitlets.Unicode()
    name = traitlets.Unicode()
```

```{code-cell} ipython3
speak_now = MusicAlbum(artist = "Taylor Swift", name = "Speak Now", year_released = 2010)
```

```{code-cell} ipython3
speak_now.artist
```

```{code-cell} ipython3
speak_now.year_released = "fourteen years ago"
```

```{code-cell} ipython3
def show_change(change):
    print("Changed {name} from {old} to {new}".format(**change))
speak_now.observe(show_change, ["name", "year_released", "artist"])
```

```{code-cell} ipython3
speak_now.year_released = 2011
```

```{code-cell} ipython3
speak_now.year_released = 2023
speak_now.name = speak_now.name + " (Taylor's Version)"
```

```{code-cell} ipython3
speak_now.year_released
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
    height = traitlets.Unicode("average")
    group_name = traitlets.Unicode()

    @traitlets.default("row_and_seat")
    def random(self):
        return (random.choice("ABCDEFG"),
                random.randint(1, 15))
```

```{code-cell} ipython3
s1, s2, s3 = Student(), Student(), Student()
```

```{code-cell} ipython3
s1.row_and_seat, s2.row_and_seat, s3.row_and_seat
```

```{code-cell} ipython3
s1.height
```

```{code-cell} ipython3
s4 = Student(row_and_seat = ('B', 1), height = "tall" )
```

```{code-cell} ipython3
s4.row_and_seat, s4.height
```

```{code-cell} ipython3
s4.traits()
```

```{code-cell} ipython3
s1.group_name
```

```{code-cell} ipython3
s2.group_name
```

```{code-cell} ipython3
traitlets.link( (s1, "group_name"), (s2, "group_name") )
```

```{code-cell} ipython3
s1.group_name = "The Mongooses"
```

```{code-cell} ipython3
s1.group_name
```

```{code-cell} ipython3
s2.group_name
```

```{code-cell} ipython3
s2.group_name = "Universe A"
```

```{code-cell} ipython3
s2.group_name
```

```{code-cell} ipython3
s1.group_name
```

```{code-cell} ipython3
class Group(traitlets.HasTraits):
    name = traitlets.Unicode()
g = Group(name = "Universe One")
```

```{code-cell} ipython3
traitlets.link( (s3, "group_name"), (g, "name"))
```

```{code-cell} ipython3
s3.group_name
```

```{code-cell} ipython3
g.name
```

```{code-cell} ipython3
g.name = "Universe One"
```

```{code-cell} ipython3
s3.group_name
```

```{code-cell} ipython3
def print_band_name(name):
    print("Band name is ", name)
```

```{code-cell} ipython3
print_band_name("The Hives")
```

```{code-cell} ipython3
print_band_name("Project")
```

```{code-cell} ipython3
import ipywidgets
```

```{code-cell} ipython3
@ipywidgets.interact(name = ["The Hives", "The Kingsmen", "The Breeders"])
def print_band_name(name):
    print("Band name is ", name)
```

```{code-cell} ipython3
@ipywidgets.interact(name = "stuff")
def print_band_name(name):
    print("Band name is ", name)
```

```{code-cell} ipython3
@ipywidgets.interact(divisor = (1, 100, .1))
def divide_by_divisor(divisor):
    print("Some value ", 217, "divided by", divisor, " = ", 217 / divisor)
```

```{code-cell} ipython3
import matplotlib.pyplot as plt
```

```{code-cell} ipython3
plt.style.available
```

```{code-cell} ipython3
@ipywidgets.interact(style = plt.style.available)
def example_plot(style):
    with plt.style.context(style):
        plt.plot([1, 2, 5.3, 9], [4, 2.1, 9, 0.4])
```

```{code-cell} ipython3
int_slider = ipywidgets.IntSlider(min = -100, max = 101)
```

```{code-cell} ipython3
int_slider
```

```{code-cell} ipython3
int_slider.min, int_slider.max
```

```{code-cell} ipython3
int_slider.value
```

```{code-cell} ipython3
bounded_int = ipywidgets.BoundedIntText(min = -100, max = 101)
```

```{code-cell} ipython3
bounded_int
```

```{code-cell} ipython3
traitlets.link((int_slider, 'value'), (bounded_int, 'value'))
```

```{code-cell} ipython3
irs = ipywidgets.IntRangeSlider(min = -1000)
```

```{code-cell} ipython3
irs.value
```

```{code-cell} ipython3
@ipywidgets.interact(bounds = irs)
def show_bounds(bounds):
    print("Spanning ", bounds[0], "to", bounds[1])
```

```{code-cell} ipython3
cp = ipywidgets.ColorPicker()
cp
```

```{code-cell} ipython3
cp.value
```

```{code-cell} ipython3
ipywidgets.DatePicker()
```

```{code-cell} ipython3
ipywidgets.Controller()
```

```{code-cell} ipython3
html = ipywidgets.HTML()
```

```{code-cell} ipython3
html
```

```{code-cell} ipython3
ta = ipywidgets.Textarea()
ta
```

```{code-cell} ipython3
ta
```

```{code-cell} ipython3
ta.value
```

```{code-cell} ipython3
traitlets.link((html, "value"), (ta, "value"))
```

```{code-cell} ipython3
sliders = [ipywidgets.IntSlider() for _ in range(10)]
```

```{code-cell} ipython3
ipywidgets.HBox(sliders)
```

```{code-cell} ipython3
ipywidgets.VBox(sliders)
```

```{code-cell} ipython3
our_display = ipywidgets.HTML()
```

```{code-cell} ipython3
our_display
```

```{code-cell} ipython3
traitlets.link((speak_now, "name"), (our_display, "value"))
```

```{code-cell} ipython3
speak_now.name = "Speak Now (Taylor's Version (Taylor's Version))"
```

```{code-cell} ipython3
my_button = ipywidgets.Button(description = "Click on me!")
```

```{code-cell} ipython3
my_button
```

```{code-cell} ipython3
class Counter(traitlets.HasTraits):
    num_clicks = traitlets.Int()
```

```{code-cell} ipython3
counter = Counter()

def click_button(b):
    counter.num_clicks += 1

my_button.on_click(click_button)
```

```{code-cell} ipython3
counter.num_clicks
```

```{code-cell} ipython3

```

```{code-cell} ipython3
l = ipywidgets.Label()
traitlets.link((counter, "num_clicks"), (l, "value"), (lambda a: str(a), lambda a: int(a)))
```

```{code-cell} ipython3
l
```

```{code-cell} ipython3
l.value = "15"
```

```{code-cell} ipython3
counter.num_clicks
```

```{code-cell} ipython3

```
