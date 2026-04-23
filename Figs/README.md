# Figure Data, Animation Scripts and Final Files

Each figure in the accompanying manuscript (found here, https://charlie-patrickson.github.io/Tutorial-Interpreting-Spin-Dynamics-in-Dynamical-Decoupling-Schemes/) describes the time-evolution of a quantum system on the Bloch sphere. The underlying time-evolution calculations are produced uing Simulation.ipynb in the Simulation_Code directory. This directory hosts the output data (labelled "Fig_xx_Sim_data.csv"), corresponding dedicated animation script (labelled "Fig_xx_GIF_script.py") and image (labelled "Fig_xx.gif") used for each figure. This README provides an overview of the constituent files, detailing required formatting of the quantum dynamics simulation data, and documentation for the visualisation/ gif scripts. Note that in some cases the final GIFs were edited in MS powerpoint (and re-exported as GIFs). 

## Quantum Dynamics Data Formatting in "Fig_xx_Sim_data.csv" Files

The "Fig_xx_Sim_data.csv" files describe the Bloch, $\bm{S}$ and effective field vectors, $\Omega_{eff}$, at a series of discrete time steps, as calculated using Simulation.ipynb in the Simulation_Code directory. The dedicated animation scripts (labelled "Fig_xx_GIF_script.py") require .csv file formats using the following headers:

Time	Sx	Sy	Sz	Hx	Hy	Hz

Optional: For simulations that include a signal field to drive a change in Bloch vector, three additional headers and columns may be included:

Signal_x	Signal_y	Signal_z

## Animation Script Documentation for "Fig_xx_GIF_script.py" Files

Each animation and function script, labelled "Fig_xx_GIF_script.py" and "Bloch_sphere_Functions" respectively, is paired with a dedicated data file, labelled "Fig_xx_Sim_data.csv". The main "Fig_xx_GIF_script.py" file: 

- defines plotting parameters/ Bloch sphere appearance
- loads the paired "Fig_xx_Sim_data.csv" file
- iterates over each row (i.e. time step)
- plots the Bloch vector and effective field on the Bloch sphere
- saves individual frames to a local `frames/` directory
- compiles these frames into a GIF

The documentation below describes the parameters, arguments and keywords used in the main "Fig_xx_GIF_script.py" file. Note that all files need to be stored in the same directory. 

<pre>
Skip_Lines = selects the time steps to plot, e.g. if Skip_Lines = 5, every 5th line of "Fig_xx_Sim_data.csv" will be plotted. 
linewidth = defines lineiwdths used to plot the Bloch sphere itself, including the solid outer line and the dashed lines that define the XY, YZ, and XZ planes, and the Bloch vector trajectory.
linestyle = linestyle used to plot the circles that define the XY, YZ, and XZ planes.
arrowhead_size = arrowhead size of the Bloch and effective field vectors
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
filenames = 
images = 
</pre>
