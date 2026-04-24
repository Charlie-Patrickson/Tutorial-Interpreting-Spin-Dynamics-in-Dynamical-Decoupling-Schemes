# Figure Data, Animation Scripts and Final Files

Each figure in the accompanying manuscript (found here, https://charlie-patrickson.github.io/Tutorial-Interpreting-Spin-Dynamics-in-Dynamical-Decoupling-Schemes/) describes the time-evolution of a quantum system on the Bloch sphere. The underlying time-evolution calculations are produced uing Simulation.ipynb in the Simulation_Code directory. This directory hosts the output data (labelled "Fig_xx_Sim_data.csv"), corresponding dedicated animation scripts (labelled "Fig_xx_GIF_script.py") and images (labelled "Fig_xx.gif") used for each figure. This README provides an overview of the constituent files, detailing required formatting of the quantum dynamics simulation data, and documentation for the visualisation/ gif scripts. Note that in some cases the final GIFs were edited in MS powerpoint (and re-exported as GIFs). 

## Quantum Dynamics Data Formatting in "Fig_xx_Sim_data.csv" Files

The "Fig_xx_Sim_data.csv" files describe the Bloch, ${S}$ and effective field vectors, $\Omega_{eff}$, at a series of discrete time steps, as calculated using Simulation.ipynb in the Simulation_Code directory. The dedicated animation scripts (labelled "Fig_xx_GIF_script.py") require .csv file formats using the following headers:

Time	Sx	Sy	Sz	Hx	Hy	Hz

Optional: For simulations that include a signal field to drive a change in Bloch vector, three additional headers and columns may be included:

Signal_x	Signal_y	Signal_z

## Animation Script Documentation for "Fig_xx_GIF_script.py" Files

This script generates Bloch sphere animations from precomputed quantum dynamics data. Each animation script (`Fig_xx_GIF_script.py`) and supporting function file (`Bloch_sphere_Functions.py`) is paired with a corresponding data file (`Fig_xx_Sim_data.csv`). The main "Fig_xx_GIF_script.py" file: 

- defines plotting parameters/ Bloch sphere appearance
- loads the paired "Fig_xx_Sim_data.csv" file
- iterates over each row (i.e. time step)
  - calls "Make_a_pretty_Bloch_sphere" to create the empty, bare Bloch sphere plot
  - calls "Plot_Bloch_trajectories" to plot:
    - the Bloch trajectory up to the current time step
    - the current Bloch vector
    - current effective field 
  - saves individual frames to a local "frames" directory
- compiles these frames into a GIF

The documentation below describes the parameters, arguments and keywords used in the main "Fig_xx_GIF_script.py" file. Note that all files need to be stored in the same directory. 

### Parameters and Variables

```text  
Skip_Lines = selects the time steps to plot, e.g. if Skip_Lines = 5, every 5th line of "Fig_xx_Sim_data.csv" will be plotted. 
linewidth = defines linewidths used to plot the Bloch sphere itself, including the solid outer line and the dashed lines that define the XY, YZ, and XZ planes, and the Bloch vector trajectory.
linestyle = linestyle used to plot the circles that define the XY, YZ, and XZ planes.
arrowhead_size = arrowhead size of the Bloch and effective field vectors
tilt_angle = optional argument, takes degrees, rotates the Bloch sphere (currently along the y and z axes simultaneously) to change appearance
Signal_Max_Y = unused
drive_colour_x = colour used for the effective field x component
drive_colour_y = colour used for the effective field y component (not used in every file, needs to be updated)
drive_colour_z = colour used for the effective field z component
Signal_color = colour used to plot the signal field if present in "Fig_xx_Sim_data.csv"
data = either loaded in "Fig_xx_Sim_data.csv" data, or a list of "Fig_xx_Sim_data.csv" data if multiple Bloch vectors are plotted at the same time
Spin_colours = colour used for the Bloch vectors, dimensions must equal "data"
Total_No_of_data_points = total number of rows (i.e. time steps) to plot
index = unused
Frame_no = initialised to 0, iterates +1 over each loop and used in the file name of each saved plot. 
ax1 = the axis used to plot the Bloch sphere itself
ax2 = optional, usually the axis used to plot the Sz component of the Bloch vector
ax3 = optional, either used to plot the effective field vector (Fig 2), or the Sx Bloch vector component (Fig. 3)
filenames = list of output images saved using the "Frame_no" variable in the "frames" folder
images = a list of all the images listed in "filenames" 
```

## Supporting `Bloch_sphere_Functions.py`

The functions defined in `Bloch_sphere_Functions.py` handle the construction of the Bloch sphere and the plotting of Bloch vector trajectories. Key functions include:

### `Make_solid_outer_circle(Tilt_angle, ax, linewidth)`
This function plots the solid outer circle of the Bloch sphere. It initially defines a circle in the YZ-plane. When `Tilt_angle ≠ 0`, the Bloch sphere is rotated (via `Make_a_pretty_Bloch_sphere`) to change the viewing perspective. To ensure the outer circle remains perpendicular to the observer, this function applies rotation matrices to the initialised circle.

#### Parameters

```text
scale - moves the circle slightly outside the Bloch sphere so it doesnt obscure the Bloch trajectory etc.
Tile_angle - given in degrees, rotates the Bloch sphere to change plot appearance
phi - 0 to 2pi used to plot complete circles

x, y, z - initialised to define a circle in the YZ-plane, facing the observer when Tilt_angle = 0

Ry - rotation matrix around the y axis, by angle Tilt_angle
Rz - rotation matrix around the z axis, by angle Tilt_angle

vector - rotated coordinates obtained by applying Ry and Rz to (x, y, z).
```

### `axis_dots(x, y, z, ax)`  
This function simply plots the axis intercepts as small circles on the Bloch sphere. 

### `plot_circle(ax, plane, radius, linestyle='solid', linewidth=1, z_position=0, phi1 = 0, phi2=2*np.pi, colour = "grey")`
This function plots the grey dashed circles defining the XY-, XZ- and YZ-planes. The function is handed a specific plane to plot a circle on.

### `Make_a_pretty_Bloch_sphere(ax, linestyle, linewidth=1, Tilt_angle=18, ax2 = None)`
This function is called from the main Fig_xx_GIF_script.py script and coordinates the construction of the Bloch sphere:

1) calls axis_dots to plot axis intercepts
2) calls plot_circle to render dashed circles in the XY, XZ, and YZ planes
3) calls Make_solid_outer_circle to render the outer boundary
4) rotates the axes by Tilt_angle
5) removes the background grid
6) sets axis limits so the Bloch sphere fills the image

linestyle = currently overrides the handed linestyle, defines the linestyle of the XY-, YZ-, XZ-plane circles. Set to (0, (8, 3)) for all plots used here. 
phi, theta, x, y, z = unused

### `Plot_Bloch_trajectories(i, Signal_color, linewidth, ax, arrowhead_size, data, drive_colour_x, drive_colour_z, Signal_Max_Y, spin_colours='k', ax2 = None, ax3 = None)`

This function is called from the main `Fig_xx_GIF_script.py` script for each selected row (i.e. time step) of the paired `Fig_xx_Sim_data.csv` file(s), and plots the Bloch vector trajectories up to the current time step, the current Bloch vector, and the current drive field on the Bloch sphere created using `Make_a_pretty_Bloch_sphere` in the same loop of the main `Fig_xx_GIF_script.py`. The function is handed all data in the paired `Fig_xx_Sim_data.csv` file(s), parses the data from each file using the headers, uses a row index passed from `Fig_xx_GIF_script.py` to identify the current step, and plots the Bloch trjectory using the passed spin colour(s), the current Bloch vector using the passed spin colour(s), the Sz component of the Bloch vector on ax2 if passed an ax2 axis, the drive field on the Bloch sphere, optionally the drive field on ax3 if passed ax3 and a signal field onto the Bloch sphere if a signal field is present in the paired `Fig_xx_Sim_data.csv` files(s).

This function is called within the main `Fig_xx_GIF_script.py` loop and is responsible for plotting the time evolution of the Bloch vector and associated fields at each time step.

For a given index `i`, corresponding to a row (i.e. time step) in the paired `Fig_xx_Sim_data.csv` file(s), the function:

- extracts `Fig_xx_Sim_data.csv` data using column headers  
- plots the Bloch trajectory on the Bloch sphere up to the current time step defined by `i`
- plots the instantaneous Bloch vector on the Bloch sphere  
- plots the effective (drive) field vector on the Bloch sphere  

Additional functionality includes:

- plotting the $S_z$ component of the Bloch vector on `ax2` (if provided)  
- plotting the effective field or $S_x$ component of the Bloch vector `ax3` (if provided)  
- plotting a signal field on the Bloch sphere if present in the data

Multiple datasets can be handled simultaneously, with colours defined by `spin_colours`.

#### Notes

- `data` may contain one or multiple datasets (e.g. for multiple Bloch vectors)  
- the function assumes input data follows the format defined in `Fig_xx_Sim_data.csv`  
- this function is called once per time step during GIF generation  

### `Arrow3D(FancyArrowPatch)`

This class enables the rendering of arrows in 3D Matplotlib plots. Since Matplotlib does not natively support true 3D arrow objects, `Arrow3D` extends the 2D `FancyArrowPatch` class and manually projects 3D coordinates onto the 2D plotting canvas. Here it is used to plot directional vectors on the Bloch sphere, including:

- the instantaneous Bloch vector
- the instantaneous effective field vector

#### How it works

- The arrow is defined by two points in 3D space (`xs`, `ys`, `zs`)
- These coordinates are stored when the object is initialised
- During rendering, the 3D coordinates are projected into 2D using Matplotlib’s internal projection system (`proj3d.proj_transform`)
- The resulting 2D coordinates are used to position a standard 2D arrow (`FancyArrowPatch`)
- A depth value is returned to ensure correct layering of objects in the 3D plot

#### Notes

- This is a projection-based method rather than true 3D rendering
- The appearance of the arrow depends on the current viewing angle of the 3D axes
- The class relies on Matplotlib’s internal projection matrix (`axes.M`)
