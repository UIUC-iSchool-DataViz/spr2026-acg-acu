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
title: CSV
---

```{code-cell} ipython3
# ! pip install matplotlib
# ! pip install numpy
# ! pip install h5py
```

```{code-cell} ipython3
import json
import h5py
import numpy as np
```

# CSV

```{code-cell} ipython3
!wget https://think.cs.vt.edu/corgis/datasets/csv/airlines/airlines.csv
```

```{code-cell} ipython3
f = 'airlines.csv'

with open(f, 'r') as fin:
    data = fin.readlines()
    
print(len(data))
```

```{code-cell} ipython3
data[0]
```

```{code-cell} ipython3
data[1]
```

```{code-cell} ipython3
data[2]
```

```{code-cell} ipython3
data[-1]
```

```{code-cell} ipython3
line = data[1].split(',')
line
```

```{code-cell} ipython3
print(line[0])
```

```{code-cell} ipython3
print(type(line[0]))
```

```{code-cell} ipython3
print(line[6])
```

```{code-cell} ipython3
print(type(line[6]))
```

# JSON

```{code-cell} ipython3
!wget https://think.cs.vt.edu/corgis/datasets/json/airlines/airlines.json
```

```{code-cell} ipython3
f = 'airlines.json'

with open(f, 'r') as fin:
    data = json.load(fin)

print(len(data))
```

```{code-cell} ipython3
data[0]
```

```{code-cell} ipython3
data[:3]
```

```{code-cell} ipython3
type(data[0])
```

```{code-cell} ipython3
one_record = data[0]
one_record.get('Airport')
```

```{code-cell} ipython3
print(type(one_record.get('Airport')))
```

```{code-cell} ipython3
total_number_of_delays = 0

for d in data:
    airport_code = d.get('Airport').get('Code')
    number_of_delay = d.get('Statistics').get('# of Delays').get('Weather')
    
    if airport_code == 'ORD':
        total_number_of_delays += number_of_delay
total_number_of_delays
```

# HDF5

```{code-cell} ipython3
!wget https://raw.githubusercontent.com/TK-Hsiao/TK-Hsiao.github.io/master/data/airlines.h5
```

```{code-cell} ipython3
def printname(name):
    print(name)
```

```{code-cell} ipython3
hf = h5py.File('airlines.h5', 'r')
print(type(hf))
```

```{code-cell} ipython3
hf.visit(printname)
```

```{code-cell} ipython3
ord_airport = hf.get('ORD')
print(ord_airport)
```

```{code-cell} ipython3
ord_airport.visit(printname)
```

```{code-cell} ipython3
print(ord_airport.get('delays_in_2003'))
```

```{code-cell} ipython3
print(np.array(ord_airport.get('delays_in_2003')))
```

```{code-cell} ipython3
hf.close()
```

```{code-cell} ipython3

```
