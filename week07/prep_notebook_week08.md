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
  display_name: Environment (conda_is590dv-default)
  language: python
  name: conda_is590dv-default
layout: notebook
title: Prep Notebook Week08
---

```{code-cell} ipython3
%matplotlib inline
```

```{code-cell} ipython3
import cartopy
import pandas as pd
import matplotlib.pyplot as plt
```

```{code-cell} ipython3
plt.rcParams["figure.dpi"] = 300
```

```{code-cell} ipython3
states = cartopy.io.shapereader.natural_earth(resolution='110m', category='cultural',
                                    name='admin_1_states_provinces_lakes_shp')
```

```{code-cell} ipython3
reader = cartopy.io.shapereader.Reader(states)
```

```{code-cell} ipython3
fig = plt.figure()
ax = fig.add_subplot(111, projection = cartopy.crs.PlateCarree())
ax.coastlines()
plt.title("Equirectangular");
```

```{code-cell} ipython3
ny_lon, ny_lat = -75, 43
```

```{code-cell} ipython3
def make_proj(proj_name):
    fig = plt.figure()
    proj = getattr(cartopy.crs, proj_name)
    ax = fig.add_subplot(111, projection = proj())
    ax.gridlines()
    ax.coastlines()
    ax.set_global()
    plt.title(proj_name)
    plt.savefig("images/{}.png".format(proj_name.lower()))
    ax.tissot(500, alpha=0.25, facecolor='red')
    plt.savefig("images/{}_tissot.png".format(proj_name.lower()))
```

```{code-cell} ipython3
for proj in ["Mercator", "PlateCarree", "Gnomonic", "TransverseMercator", "LambertCylindrical", "Mollweide", "Sinusoidal"]:
    make_proj(proj)
    print("Done with", proj)
```

```{code-cell} ipython3
champaign_lat, champaign_lon = 40.1164, -88.2434
antananarivo_lat, antananarivo_lon = -18.8792, 47.5079
```

```{code-cell} ipython3
fig = plt.figure()
ax = fig.add_subplot(111, projection = cartopy.crs.PlateCarree())
ax.gridlines()
ax.coastlines()
ax.set_global()
ax.plot([champaign_lon, antananarivo_lon], [champaign_lat, antananarivo_lat], transform = cartopy.crs.PlateCarree())
ax.plot([champaign_lon, antananarivo_lon], [champaign_lat, antananarivo_lat], transform = cartopy.crs.Geodetic())
```

```{code-cell} ipython3
fig = plt.figure()
ax = fig.add_subplot(111, projection = cartopy.crs.Mollweide())
ax.gridlines()
ax.coastlines()
ax.set_global()
ax.plot([champaign_lon, antananarivo_lon], [champaign_lat, antananarivo_lat], transform = cartopy.crs.PlateCarree())
ax.plot([champaign_lon, antananarivo_lon], [champaign_lat, antananarivo_lat], transform = cartopy.crs.Geodetic())
```

```{code-cell} ipython3

```
