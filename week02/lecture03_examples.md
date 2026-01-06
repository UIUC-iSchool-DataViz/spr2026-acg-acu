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
title: Lecture03 Examples
---

![]( https://uiuc-ischool-dataviz.github.io/spring2019online/week01/images/stitch_reworked.png)

```{code-cell} ipython3
!wget https://uiuc-ischool-dataviz.github.io/spring2019online/week01/images/stitch_reworked.png
```

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image
```

```{code-cell} ipython3
%matplotlib inline
```

```{code-cell} ipython3
plt.plot([1, 2, 3, 5], [4, 1, 2, 9])
```

```{code-cell} ipython3
im = PIL.Image.open("stitch_reworked.png")
```

```{code-cell} ipython3
im
```

```{code-cell} ipython3
type(im)
```

```{code-cell} ipython3
im_data = np.array(im)
```

```{code-cell} ipython3
im_data.shape
```

```{code-cell} ipython3
im_data.dtype
```

```{code-cell} ipython3
im_data[240, 210, 0]
```

```{code-cell} ipython3
im_data[240, 210, :]
```

```{code-cell} ipython3
im_data[ 230:240, 210, 1 ]
```

```{code-cell} ipython3
arr = np.arange(100)
```

```{code-cell} ipython3
arr
```

```{code-cell} ipython3
arr[4:10]
```

```{code-cell} ipython3
arr[:5]
```

```{code-cell} ipython3
arr[4:10:2]
```

```{code-cell} ipython3
arr[::-1]
```

```{code-cell} ipython3
PIL.Image.fromarray(im_data[:250:-1, :, :])
```

```{code-cell} ipython3
im_data.shape
```

```{code-cell} ipython3
im_data.reshape(-1, im_data.shape[2]).shape
```

```{code-cell} ipython3
483*430
```

```{code-cell} ipython3
np.unique([1, 2, 3, 1, 1, 1])
```

```{code-cell} ipython3
np.unique(im_data.reshape(-1, im_data.shape[2]), axis=0)
```

```{code-cell} ipython3
plt.imshow(im_data)
```

```{code-cell} ipython3
fig, ax = plt.subplots(figsize = (5,5))
ax.set_facecolor("gray")
ax.imshow(im_data)

plt.show()
```

```{code-cell} ipython3

```
