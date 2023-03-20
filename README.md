# AE 6102 - Parallel Scientific Computing and Visualization
# Project - Orbit Propogation of Satellites

## Meet the team :-

| Name                   | Roll No.  | Contribution |
| ---------------------- | --------- | ------------ |
| Karthikeya Reddy konda | 190050060 |              |
| Kartikeya Gupta        | 190050044 |              |
| Akash Reddy G          | 190050038 |              |

## Abstract

Determining future position of a satellite given current position and velocity is theoretically a difficult task, involving differential equations which are not analytically solvable in time.

Hence simulations are the only way . However there exist various methods of simulating this physical phenomenon. Some are computationally intensive and accurate and some are less but faster in simulation.

## Outline

- We plan to implement a simple method in orbit propagation. Using a naive way ( such as for loop in python for each time step dt in the differential equations ) and then optimize the code further using numba (e.g. python for loops) comparing the time taken to simulate a particular event in both cases. Show graphically how fast are the improvements ( say a graph with y-axis : computation time taken, x-axis : no of timesteps)

- Then we plan to build a visualization of a computed satellite path for a fixed time interval and use some of the standard libraries. Using automan run simulations of various initial conditions and accordingly visualize all the paths in the visualization 

- Can repeat the above point in case of 3 body systems ( say a binary star and a satellite ). Using automan exploring various initial conditions for which a stable orbit may form.

- In case of multiple satellites, can encode all objects dynamic equations in vector form ( all position co-ordinates in a single vector and imagine differential equation in this vector ) and demonstrate simulation performance enhancement by using single core, multi core, GPU.





