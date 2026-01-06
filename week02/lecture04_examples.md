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
title: Examples for Lecture 4
---

# Examples for Lecture 4

We will be covering two principal areas:

 * A few types of aggregation -- counting, average, weighted average, sum
 * The "building inventory" dataset, and some simple pandas operations on it

```{code-cell} ipython3
!wget https://uiuc-ischool-dataviz.github.io/spring2019online/week02/building_inventory.csv
```

```{code-cell} ipython3
%matplotlib inline
```

```{code-cell} ipython3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

```{code-cell} ipython3
df = pd.read_csv("building_inventory.csv")
```

```{code-cell} ipython3
df.columns
```

```{code-cell} ipython3
df.dtypes
```

```{code-cell} ipython3
df.head()
```

```{code-cell} ipython3
df.describe()
```

```{code-cell} ipython3
df.shape
```

```{code-cell} ipython3
(df["Year Acquired"] == 0).sum()
```

```{code-cell} ipython3
(df["Year Constructed"] == 0).sum()
```

```{code-cell} ipython3
(df["Square Footage"] == 0).sum()
```

```{code-cell} ipython3
df = pd.read_csv("building_inventory.csv", na_values={
    "Year Acquired": 0,
    "Year Constructed": 0,
    "Square Footage": 0
})
```

```{code-cell} ipython3
df.describe()
```

```{code-cell} ipython3
plt.plot([1,2,3,4], [5, 1, 2, 4], "-o")
```

```{code-cell} ipython3
plt.rcParams["figure.dpi"] = 200
```

```{code-cell} ipython3
plt.plot(df["Year Constructed"], df["Year Acquired"], '.')
plt.xlabel("Year Constructed")
plt.ylabel("Year Acquired")
```

```{code-cell} ipython3
df["Age at Acquisition"] = df["Year Acquired"] - df["Year Constructed"]
```

```{code-cell} ipython3
df["Age at Acquisition"].describe()
```

```{code-cell} ipython3
old_buildings = df[
    df["Age at Acquisition"] >= 0
]
```

```{code-cell} ipython3
plt.hist(old_buildings["Age at Acquisition"], log=True)
plt.xlabel("Age at Acquisition")
plt.ylabel("Count")
```

```{code-cell} ipython3
df["Agency Name"].unique()
```

```{code-cell} ipython3
df_by_agency = df.groupby("Agency Name")
```

```{code-cell} ipython3
for agency_name, new_df in df_by_agency:
    print(agency_name, new_df.shape)
```

```{code-cell} ipython3
df_by_agency["Square Footage"].sum()
```

```{code-cell} ipython3

```

```{code-cell} ipython3

```
