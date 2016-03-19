# Generating unstructured grid

This repository contains python codes which implement a simple method of unstructured grid generation. This is an implementation of [method proposed by Saied and Alireza](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwiW0cb5u8vLAhUGkYMKHSJDC4cQFgghMAA&url=http%3A%2F%2Fwww.wseas.us%2Fe-library%2Ftransactions%2Ffluid%2F2009%2F31-810.pdf&usg=AFQjCNHHJUia2Dyj7JAbqchWqv5h83cCAw&sig2=lCboi2NRBoLp0yOtPoZ_ag). This work was done by me, Raghuvir and Gaurav as a term paper project for course Advanced Computational Fluid Dynamics.

## Input
Input was given as points, vertex (cell) connectivity matrix and edge connectivity matrix. Please go through the reference paper to understand the format. For visualization input looked like this:

## Codes
* `unstructured_grid_v3.py` : Basic implementation
* `edge_swap.py` : quality improvement by edge swapping (should be run after `unstructured_grid_v3.py`)
* `point_smooth.py` : quality improvement by point smoothening (should be run after `unstructured_grid_v3.py`)
* `geo_treat.py` : a proof of concept implementation of geometry adaptability, this changes grids for square cylinder to grids for circular cylinder
* `input.py`, `angle_measure.py` : provide some helper functions

## Output

* Vanilla implementation of algorithm (without any quality improvement) gives following grid structure:
![alt tag](https://raw.githubusercontent.com/Adarsh-Barik/UnstructuredGrid/master/images/no_quality.png)
* We can improve grid structure by edge swapping:
![alt tag](https://raw.githubusercontent.com/Adarsh-Barik/UnstructuredGrid/master/images/edge_swap.png)
* Quality can be improved even further by point smoothening:
![alt tag](https://raw.githubusercontent.com/Adarsh-Barik/UnstructuredGrid/master/images/point_smooth.png)
* Example of geometric adaptability:
![alt tag](https://raw.githubusercontent.com/Adarsh-Barik/UnstructuredGrid/master/images/geo_no_quality.png)
![alt tag](https://raw.githubusercontent.com/Adarsh-Barik/UnstructuredGrid/master/images/geo_cylinder.png)
![alt tag](https://raw.githubusercontent.com/Adarsh-Barik/UnstructuredGrid/master/images/geo_edge_swap.png)
![alt tag](https://raw.githubusercontent.com/Adarsh-Barik/UnstructuredGrid/master/images/geo_point_smooth.png)
