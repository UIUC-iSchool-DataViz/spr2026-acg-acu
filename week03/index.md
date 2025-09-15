---
layout: week
visible: true
icon: undraw_cohort_analysis_stny.svg
notitle: true
examples:
  - filename: lecture05_examples.ipynb
    type: ipynb
    title: Matplotlib specifics
    description: This goes over some very specific aspects of matplotlib, and how to apply data transformations to patches and annotations, as well as modifying properties of the plot.
  - filename: lecture06_examples.ipynb
    type: ipynb
    title: Colormaps
    description: We load in a brain scan and try some basics of colormapping in matplotlib.
  - filename: prep_notebook_week03.ipynb
    type: ipynb
    title: Prep Notebook, Week 3
    description: Prep notebook for this week
  - filename: inClass_week03-spr2025.ipynb
    type: ipynb
    title: In class notebook, Week 3, Spring 2025
    description: In class work from Spring 2025 week 03
  - filename: inClass_week03.ipynb
    type: ipynb
    title: In class notebook, Week 3
    description: Prep notebook for this week
  - filename: fall2019_prep_notebook_furtherExamples_01.ipynb
    type: ipynb
    title: fall2019_prep_notebook_furtherExamples_01.ipynb
    description: Extra notebook from 2019 class
  - filename: fall2019_prep_notebook_furtherExamples_02.ipynb
    type: ipynb
    title: fall2019_prep_notebook_furtherExamples_02.ipynb
    description: Extra notebook from 2019 class
  - filename: fall2019_prep_notebook_furtherExamples_03.ipynb
    type: ipynb
    title: fall2019_prep_notebook_furtherExamples_03.ipynb
    description: Extra notebook from 2019 class
  - filename: spring2019_prep_notebook_furtherExamples_week03.ipynb
    type: ipynb
    title: spring2019_prep_notebook_furtherExamples_week03.ipynb
  - filename: spring2019_prep_notebook_week03_part1.ipynb
    type: ipynb
    title: spring2019_prep_notebook_week03_part1.ipynb
  - filename: spring2019_prep_notebook_week03_part2.ipynb
    type: ipynb
    title: spring2019_prep_notebook_week03_part2.ipynb
data:
  - filename: building_inventory.csv
    type: dataLink
    title: Buildings dataset
    description: Illinois buildings dataset
    link: https://github.com/UIUC-iSchool-DataViz/is445_data/raw/main/building_inventory.csv
  - filename: michigan_lld.flt
    type: dataLink
    title: Michigan Depth Map (86Mb)
    description: Measurments taken from around Lake Michigan (https://www.ngdc.noaa.gov/mgg/greatlakes/michigan.html)
    link: https://github.com/UIUC-iSchool-DataViz/is445_data/raw/main/michigan_lld.flt
  - filename: single_dicom.h5
    type: dataLink
    title: Brain Scan (72Mb)
    description: MRI scan of a brain
    link: https://github.com/UIUC-iSchool-DataViz/is445_data/raw/main/single_dicom.h5
library:
  - filename: palette_colors.py
    type: library
    title: Palette Colors (palette_colors.py)
    description: Python library, save to notebook folder or modify your path if you know how to do that
---

# Transformations and Colors

This week, we covered how transformations work, how colors work, and how we can
choose transforms and colors to better suit our data.

## References and Reading List

 * [Pandas vs. Matplotlib](http://jonathansoma.com/lede/algorithms-2017/classes/fuzziness-matplotlib/understand-df-plot-in-pandas/)
 * [RGB color triplets](https://www.rapidtables.com/web/color/RGB_Color.html)
 * VAD, Ch. 10: Map Color and Other Channels 
 * [FDV, Ch. 4: Color Scales](https://serialmentor.com/dataviz/color-basics.html)
 * VAD, Ch. 5: Marks and Channels 
 * [Perception in Visualization](https://www.csc2.ncsu.edu/faculty/healey/PP/)
 * [Palettable Docs](https://jiffyclub.github.io/palettable/#documentation)

## Quick Reference for Matplotlib

Developed and available at [github.com/matplotlib/cheatsheets](https://github.com/matplotlib/cheatsheets)

 * [Cheatsheet 1](cheatsheets-1.png)
 * [Cheatsheet 2](cheatsheets-2.png)
 * [Handout for Beginners](handout-beginner.png)
 * [Handout for Intermediate Users](handout-intermediate.png)
 * [Handout with Tips](handout-tips.png)
