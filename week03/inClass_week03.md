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
title: In Class Notebook, Week 03
---

# In Class Notebook, Week 03

+++

You can access this notebook in near-realy time by going here:

https://github.com/UIUC-iSchool-DataViz/is445_bcubcg_fall2023/blob/master/week03/inClass_week03.ipynb 

Or by pasting that URL into the nbviewer interface for a plain-text rendering:

https://kokes.github.io/nbviewer.js/viewer.html

```{code-cell} ipython3
import pandas as pd
```

```{code-cell} ipython3
buildings = pd.read_csv('https://github.com/UIUC-iSchool-DataViz/is445_data/raw/main/building_inventory.csv')
```

```{code-cell} ipython3
buildings
```

```{code-cell} ipython3
buildings.index
```

```{code-cell} ipython3
buildings.iloc[5:8]
```

```{code-cell} ipython3
buildings.iloc[5:8]["Agency Name"]
```

```{code-cell} ipython3
buildings['Agency Name'].nunique()
```

```{code-cell} ipython3
buildings['Bldg Status'].unique()
```

```{code-cell} ipython3
buildings.describe() # for R users this is like the "summary"
```

```{code-cell} ipython3
buildings['Square Footage'] == 0
```

```{code-cell} ipython3
buildings.loc[buildings['Square Footage']==0]
```

```{code-cell} ipython3
import matplotlib.pyplot as plt
```

```{code-cell} ipython3
buildings['Square Footage'].plot()
plt.show()
```

```{code-cell} ipython3
buildings['Square Footage'].plot(figsize=(10,3))
plt.show()
```

```{code-cell} ipython3
buildings.plot(x='Address', y='Square Footage', figsize=(10,3), rot=90)
plt.show()
```

```{code-cell} ipython3
ax = buildings.plot(x='Year Acquired', y='Square Footage', 
                    figsize=(10,3),kind='scatter')
ax.set_xlim(1750,2020)
plt.show()
```

```{code-cell} ipython3
buildings = pd.read_csv('https://github.com/UIUC-iSchool-DataViz/is445_data/raw/main/building_inventory.csv',
                       na_values = {'Square Footage':0,
                                   'Year Acquired':0,
                                   'Year Constructed':0})
```

```{code-cell} ipython3
ax = buildings.plot(x='Year Acquired', y='Square Footage', 
                    figsize=(10,3),kind='scatter')
#ax.set_xlim(1750,2020)
plt.show()
```

```{code-cell} ipython3
buildings.describe()
```

```{code-cell} ipython3
buildings['Bldg Status'].unique()
```

```{code-cell} ipython3
buildings.groupby('Bldg Status')
```

```{code-cell} ipython3
for group in buildings.groupby('Bldg Status'):
    print(group)
```

```{code-cell} ipython3
for group_name, group_df in buildings.groupby('Bldg Status'):
    print(group_name, group_df.shape)
```

```{code-cell} ipython3
buildings2 = buildings.sort_values("Year Constructed")
```

```{code-cell} ipython3
buildings2.iloc[0]
```

```{code-cell} ipython3
agg = buildings.groupby("Year Acquired")['Square Footage'].sum()
# for each Year Acquired, what is the total (sum) of the Square Footage

#agg = buildings.groupby("Year Acquired")['Square Footage'].mean()
# for each Year Acquired, what is the average (mean) of the Square Footage
```

```{code-cell} ipython3
agg
```

```{code-cell} ipython3
type(agg)
```

```{code-cell} ipython3
type(buildings)
```

```{code-cell} ipython3
agg.index
```

```{code-cell} ipython3
agg.values
```

```{code-cell} ipython3
fig, ax = plt.subplots(figsize=(15,4))

ax.plot(agg.index, agg.values)
ax.set_xlabel('Year Constructed')
ax.set_ylabel('Total (sum) Square Footage')

plt.show()
```

```{code-cell} ipython3
agg.plot()
```

```{code-cell} ipython3
stats = buildings.groupby('Year Acquired')['Square Footage'].describe()
```

```{code-cell} ipython3
stats
```

```{code-cell} ipython3
type(stats)
```

```{code-cell} ipython3
stats.plot(y='count')
```

```{code-cell} ipython3
stats.columns
```

```{code-cell} ipython3
buildings
```

```{code-cell} ipython3
buildings['Zip code'].value_counts()
```

```{code-cell} ipython3
buildings['Zip code'].value_counts().iloc[0:5]
```

```{code-cell} ipython3
buildings['Zip code'].value_counts().iloc[0:5].index # 5 most common zipcodes in my dataframe
```

```{code-cell} ipython3
most_common_zips = buildings['Zip code'].value_counts().iloc[0:5].index
most_common_zips
```

```{code-cell} ipython3
# Check out the ".isin" function for some examples that might be useful <-- HINT
```

```{code-cell} ipython3
gb1 = buildings.groupby('Bldg Status')['Year Acquired'].min()
```

```{code-cell} ipython3
gb1
```

```{code-cell} ipython3
fig_gb1, ax_gb1 = plt.subplots()
gb1.plot(kind='bar', ax=ax_gb1)
plt.show()
```

```{code-cell} ipython3
fig_gb1, ax_gb1 = plt.subplots()
ax_gb1.bar(gb1.index, gb1.values)
plt.show()
```

```{code-cell} ipython3
ax_gb1.bar?
```

```{code-cell} ipython3

```
