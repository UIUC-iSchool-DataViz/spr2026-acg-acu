---
title: vega-lite example 4
description: Applying filtering, hconcat, layers and selections
layout: vegalite_example
---

{
"$schema": "https://vega.github.io/schema/vega-lite/v5.json",
"data": {"url": "data/cars.json"},
"hconcat": [
{
"mark": {"type": "circle"},
"params": [
{
"name": "clickanddrag",
"select": {"type": "interval", "encodings": ["y"]}
}
],
"encoding": {
"x": {"field": "Horsepower", "type": "quantitative"},
"y": {"field": "Miles_per_Gallon", "type": "quantitative"},
"tooltip": [
{"field": "Cylinders", "type": "ordinal"},
{"field": "Weight_in_lbs", "type": "quantitative"}
],
"opacity": {
"condition": {
"param":"clickanddrag"
},
"value": 0.2
}
}
},
{
"layer": [
{
"mark": "bar",
"encoding": {
"x": {"field": "Cylinders", "type": "ordinal"},
"y": {"aggregate": "count", "type": "quantitative"},
"opacity": {"value": 0.2}
}
},
{
"mark": "bar",
"transform": [{"filter": {"param": "clickanddrag"}}],
"encoding": {
"x": {"field": "Cylinders", "type": "ordinal"},
"y": {"aggregate": "count", "type": "quantitative"}
}
}
]
}
]
}
