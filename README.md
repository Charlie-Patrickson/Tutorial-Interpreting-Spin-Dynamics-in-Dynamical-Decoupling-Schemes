# Tutorial-Interpreting-Spin-Dynamics-in-Dynamical-Decoupling-Schemes


A scientific publication serving as a tutorial to educate the reader on how to interpret and visualise quantum dynamics in two-level systems. This repository hosts the simulation code, the output data, and the visualisation code used to produce every figure in the accompanying manuscript, enabling the reader to reproduce or amend our results. Read the publication here: https://charlie-patrickson.github.io/Tutorial-Interpreting-Spin-Dynamics-in-Dynamical-Decoupling-Schemes/

This repository is intended to hold a (mostly) self-contained scientific publication. The repository is structured into three main directories:


**Simulation_Code** - scripts and models used to calculate the time-evolution of each quantum system presented in the manuscript <br>
**Figures** - hosts the simulated quantum dynamics output data, and visualisation code (i.e. gif making code) used to produce each figure in the accompanying manuscript. See /Figures/README.md for code documentation, including data formats, dependencies and script structure. <br>
**Supporting code** - HTML, JavaScript, and CSS files, along with supporting assets (e.g. index.html, appendix.html). Based in part on work by Andrew G. York (CC BY 4.0): https://github.com/AndrewGYork/gfp_magnetofluorescence <br>


CODING TO-DO

1) Produce independent y and z tilt angles on the Bloch sphere
2) The handed linestyle is currently overridden directly in "Make_a_pretty_Bloch_sphere", change this, line 86
3) Remove scatter points added in "Make_a_pretty_Bloch_sphere" line 97 and as currently hidden by axis dots (as preferred)
4) phi, theta, x, y, z all unused in "Make_a_pretty_Bloch_sphere", lines 88 - 94
5) Plot the Bloch sphere before the initial loop and pass to the loop each time
6) Normalise effective field vector sizes
7) Remove unused variables: Max_Signal_Y, index in main GIF scripts
8) Add drive Y colour as standard
9) Pass plot_circle a list of planes so that it is only called once instead of three times
10) Comment code

MANUSCRIPT TO-DO

1) Add paragraphs
2) Work out citations
3) Work out self referencing
