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
title: Lecture06 Examples
---

```{code-cell} ipython3
%matplotlib inline
```

```{code-cell} ipython3
import matplotlib.pyplot as plt
import numpy as np
```

```{code-cell} ipython3
import PIL.Image
```

```{code-cell} ipython3
!wget https://uiuc-ischool-dataviz.github.io/fall2020-BOG-BOU/week03/images/winter_scene.jpg
```

```{code-cell} ipython3
image = PIL.Image.open("winter_scene.jpg")
```

```{code-cell} ipython3
image
```

```{code-cell} ipython3
arr = np.array(image)
```

```{code-cell} ipython3
arr.shape
```

```{code-cell} ipython3
flat_image = arr.reshape((-1, 3))
```

```{code-cell} ipython3
flat_image.shape
```

```{code-cell} ipython3
flat_image[:10]
```

```{code-cell} ipython3
red_only = arr.copy()
red_only[:, :, 1] = 0
red_only[:, :, 2] = 0

green_only = arr.copy()
green_only[:, :, 0] = 0
green_only[:, :, 2] = 0

blue_only = arr.copy()
blue_only[:, :, 0] = 0
blue_only[:, :, 1] = 0

r_img = PIL.Image.fromarray(red_only)
g_img = PIL.Image.fromarray(green_only)
b_img = PIL.Image.fromarray(blue_only)
```

```{code-cell} ipython3
r_img
```

```{code-cell} ipython3
g_img
```

```{code-cell} ipython3
b_img
```

```{code-cell} ipython3
fig, ax = plt.subplots(2, 1, dpi = 300)
ax[0].imshow(arr)
ax[1].hist(flat_image[:,0], bins = np.arange(256), alpha=0.5, facecolor = 'red');
ax[1].hist(flat_image[:,1], bins = np.arange(256), alpha=0.5, facecolor = 'green');
ax[1].hist(flat_image[:,2], bins = np.arange(256), alpha=0.5, facecolor = 'blue');
```

```{code-cell} ipython3
!wget https://uiuc-ischool-dataviz.github.io/spring2019online/week05/data/single_dicom.h5
```

```{code-cell} ipython3
import h5py
```

```{code-cell} ipython3
f = h5py.File("single_dicom.h5")
```

```{code-cell} ipython3
list(f.keys())
```

```{code-cell} ipython3
scan = f["scan"][:]
```

```{code-cell} ipython3
scan.shape
```

```{code-cell} ipython3
scan[18, :, :].shape
```

```{code-cell} ipython3
plt.rcParams["figure.dpi"] = 150
```

```{code-cell} ipython3
import matplotlib.colors as mc
```

```{code-cell} ipython3
import ipywidgets
```

```{code-cell} ipython3
my_norm = mc.LogNorm(vmin = 1.0, vmax = scan.max())
```

```{code-cell} ipython3
image = plt.imshow(scan[12,:,:], extent = [0, 1, 0, 1], norm=my_norm)
image.cmap.set_bad("white")
plt.colorbar()
```

```{code-cell} ipython3
@ipywidgets.interact(slice_coord = (0, 35), colormap = ["viridis", "magma", "cubehelix"])
def slice_scan(slice_coord, colormap = "viridis"):
    image = plt.imshow(scan[slice_coord,:,:], extent = [0, 1, 0, 1], norm=my_norm, cmap = colormap)
    plt.colorbar()
```

```{code-cell} ipython3

```
