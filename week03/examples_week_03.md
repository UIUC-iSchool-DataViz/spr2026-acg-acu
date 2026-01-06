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
title: Examples Week 03
---

```{code-cell} ipython3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
```

```{code-cell} ipython3
df = pd.read_csv("../data/building_inventory.csv",
                na_values = {'Year Acquired': 0,
                             'Year Constructed': 0,
                             'Square Footage': 0})
```

```{code-cell} ipython3
df.describe()
```

```{code-cell} ipython3
df.columns
```

```{code-cell} ipython3
df.groupby("Year Acquired")["Square Footage"].sum()
```

```{code-cell} ipython3
df.groupby("Year Acquired")["Square Footage"].describe()
```

```{code-cell} ipython3
stats = df.groupby("Year Acquired")["Square Footage"].describe()
```

```{code-cell} ipython3
stats.iloc[0]
```

```{code-cell} ipython3
stats.loc[1753]
```

```{code-cell} ipython3
stats.iloc[0:1]
```

```{code-cell} ipython3
stats.loc[1753:1802]
```

```{code-cell} ipython3
p = stats["max"].plot()
p.set_yscale("log")
p.set_ylabel("Square Footage")
```

```{code-cell} ipython3
plt.rcParams["figure.dpi"] = 150
```

```{code-cell} ipython3
p = stats["max"].plot()
p.set_yscale("log")
p.set_ylabel("Square Footage")
```

```{code-cell} ipython3
plt.plot(stats["min"], marker='.', linewidth=1.0, label="Min")
plt.plot(stats["max"], marker='.', linewidth=1.0, label="Max")
plt.fill_between(stats.index, stats["min"], stats["max"], color="#dddddd")
plt.yscale("log")
plt.legend()
```

```{code-cell} ipython3
plt.style.available
```

```{code-cell} ipython3
with plt.style.context("ggplot"):
    plt.plot(stats["min"], marker='.', label="Min")
    plt.plot(stats["max"], marker='.', label="Max")
    plt.fill_between(stats.index, stats["min"], stats["max"], color = "#aaaaaa")
    plt.ylabel("Square Footage")
    plt.yscale("log")
    plt.legend()
```

```{code-cell} ipython3
import matplotlib.transforms as mpt
```

```{code-cell} ipython3
with plt.style.context("ggplot"):
    plt.plot(stats["min"], marker='.', label="Min")
    plt.plot(stats["max"], marker='.', label="Max")
    plt.fill_between(stats.index, stats["min"], stats["max"], color = "#aaaaaa")
    
    plt.ylabel("Square Footage")
    plt.yscale("log")
    plt.legend()
    
    ax = plt.gca()
    plt.plot([0.5, 0.5], [0.0, 1.0], color = 'black', linewidth=2.0,
             transform = ax.transAxes)
```

```{code-cell} ipython3
with plt.style.context("ggplot"):
    plt.plot(stats["min"], marker='.', label="Min")
    plt.plot(stats["max"], marker='.', label="Max")
    plt.fill_between(stats.index, stats["min"], stats["max"], color = "#aaaaaa")
    
    plt.ylabel("Square Footage")
    plt.yscale("log")
    plt.legend()
    
    ax = plt.gca()
    new_transform = mpt.blended_transform_factory(ax.transData, ax.transAxes)
    plt.plot([1818, 1818], [0.0, 1.0], color = 'black', linewidth=2.0,
             transform = new_transform)
```

```{code-cell} ipython3
import ipywidgets
```

```{code-cell} ipython3
slider = ipywidgets.IntSlider(10)
```

```{code-cell} ipython3
slider
```

```{code-cell} ipython3
slider
```

```{code-cell} ipython3
slider.value
```

```{code-cell} ipython3
slider.min, slider.max
```

```{code-cell} ipython3
slider.min = 50
```

```{code-cell} ipython3
ipywidgets.IntSlider(10, min = 9, max=11)
```

```{code-cell} ipython3
@ipywidgets.interact(style = plt.style.available, min_x = (0.0, 10.0, 0.1))
def make_plot(style = "ggplot", min_x = 0.0):
    with plt.style.context(style):
        plt.plot([1,2,3,4], [5,3,1,4])
        plt.xlim(min_x, 15.0)
```

```{code-cell} ipython3
make_plot("fivethirtyeight")
```

```{code-cell} ipython3
plt.scatter("Year Acquired", "Year Constructed", data = df)
```

```{code-cell} ipython3
plt.scatter(df["Year Acquired"], df["Year Acquired"] - df["Year Constructed"])
```

```{code-cell} ipython3
df["Delta Time"] = df["Year Acquired"] - df["Year Constructed"]
df["Delta Time"].replace(0, np.nan, inplace=True)
```

```{code-cell} ipython3
plt.subplot(4, 5, 1)
plt.plot([1,2,3], [2,3,4])
plt.subplot(4, 5, 19)
plt.plot([1,2,3], [1,1,1])
```

```{code-cell} ipython3
michigan = np.fromfile("michigan_lld/michigan_lld.flt", dtype="f4").reshape((5365, 4201))
```

```{code-cell} ipython3
michigan.shape
```

```{code-cell} ipython3
michigan.max()
```

```{code-cell} ipython3
michigan.min()
```

```{code-cell} ipython3
michigan[michigan == -9999] = np.nan
```

```{code-cell} ipython3
plt.hist(michigan.flat)
```

```{code-cell} ipython3
np.nanmin(michigan), np.nanmax(michigan)
```

```{code-cell} ipython3
plt.imshow(michigan)
plt.colorbar(extend = 'both')
plt.clim(-352, 352)
```

```{code-cell} ipython3
plt.imshow(michigan, cmap="seismic")
plt.colorbar(extend = 'both')
plt.clim(-352, 352)
```

```{code-cell} ipython3
plt.imshow(michigan, cmap="jet")
plt.colorbar(extend = 'both')
plt.clim(-352, 352)
```

```{code-cell} ipython3
import matplotlib.colors as colors
```

```{code-cell} ipython3
plt.imshow(np.abs(michigan), norm = colors.LogNorm())
plt.colorbar(extend='both')
```

```{code-cell} ipython3
plt.imshow(michigan, norm = colors.SymLogNorm(100), cmap="terrain")
plt.colorbar(extend='both')
```

```{code-cell} ipython3
plt.imshow(michigan, norm = colors.SymLogNorm(100), cmap="terrain")
plt.xlim(2700, 3300)
plt.ylim(3300, 3900)
plt.colorbar(extend='both')
```

```{code-cell} ipython3
x0 = -88.0
y0 = 46.09
dx = 0.000833333333
dy = 0.000833333333
```

```{code-cell} ipython3
plt.imshow(michigan, extent = [x0, x0 + dx * michigan.shape[0],
                               y0, y0 + dy * michigan.shape[1]],
          norm = colors.SymLogNorm(10), cmap="terrain")
plt.colorbar()
```

```{code-cell} ipython3
y0, x0
```

```{code-cell} ipython3

```
