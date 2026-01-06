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
title: Examples Week10
---

```{code-cell} ipython3
import bqplot
import json
import numpy as np
import pandas as pd
```

```{code-cell} ipython3
tree_data = json.load(open("../workspace/champaign_trees.geojson", "r"))
```

```{code-cell} ipython3
tree_data.keys()
```

```{code-cell} ipython3
tree_data['type']
```

```{code-cell} ipython3
len(tree_data['features'])
```

```{code-cell} ipython3
tree_data['features'][0]
```

```{code-cell} ipython3
sc_map = bqplot.AlbersUSA()
sc_color = bqplot.ColorScale()
us_map = bqplot.Map(map_data = bqplot.topo_load("map_data/USStatesMap.json"),
                           scales = {'projection': sc_map,
                                    "color": sc_color},
                    colors = {"default_color": "black"},
                    color = {_:_ for _ in np.arange(100)})

fig = bqplot.Figure(marks = [us_map])

display(fig)
```

```{code-cell} ipython3
import ipywidgets
```

```{code-cell} ipython3
l = ipywidgets.Label()
def change_label(event):
    l.value = str(event['new'])

champaign_map.observe(change_label, ["selected"])
l
```

```{code-cell} ipython3

```

```{code-cell} ipython3
legislators = pd.read_csv("../workspace/legislators_historical.csv")
```

```{code-cell} ipython3
legislators_terms = pd.read_csv("../workspace/legislators_historical_terms.csv")
```

```{code-cell} ipython3
fips = pd.read_csv("../workspace/state_fips_master.csv")
```

```{code-cell} ipython3
legislators_terms.state
```

```{code-cell} ipython3
fips_lookup = {row['state_abbr']: row['fips'] for _, row in fips.iterrows()}
```

```{code-cell} ipython3
legislators_fips = legislators_terms.replace({"state": fips_lookup})
```

```{code-cell} ipython3
colors = dict(legislators_fips.groupby("state").count()["bioguide"])
```

```{code-cell} ipython3
sc_map = bqplot.AlbersUSA()
sc_color = bqplot.ColorScale(scheme = "Blues")
us_map = bqplot.Map(map_data = bqplot.topo_load("map_data/USStatesMap.json"),
                           scales = {'projection': sc_map,
                                    "color": sc_color},
                    colors = {"default_color": "black"},
                    color = colors)

fig = bqplot.Figure(marks = [us_map])

display(fig)
```

```{code-cell} ipython3

```
