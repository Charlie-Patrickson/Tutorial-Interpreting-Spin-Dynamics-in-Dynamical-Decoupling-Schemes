# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 19:49:22 2025

@author: cp728
"""

import Bloch_sphere_functions as BSfcs
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import imageio.v2 as imageio
import os

from matplotlib import rcParams
plt.rcParams['mathtext.fontset'] = 'dejavuserif'
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.sans-serif'] = ['Cambria math', 'sans-serif']

output_dir = "frames"
os.makedirs(output_dir, exist_ok=True)  # Only creates it if it doesn't already exist

Skip_lines = 0
linewidth = 2
linestyle = "solid"
arrowhead_size = 32
Signal_Max_Y = 0.75
drive_colour_z = "#2F9E84"
drive_colour_x = "#2C5AB6"
Signal_color = "#218D8C"
Spin_colours = ['k', 'dimgrey', 'grey', 'darkgrey', 'lightgrey']

data = [pd.read_csv("Fig_1c_Sim_data.csv")]
Total_No_of_data_points = 100

index = 0
Frame_no = 0

for i in range(0, Total_No_of_data_points, Skip_lines+1):
    
    fig = plt.figure(figsize=(20,8))
    ax1 = fig.add_subplot(121, projection='3d',computed_zorder=False)
    
    ax2 = None
    
    '''
    ax2 = fig.add_subplot(122)
    ax2.set_xlabel(f"Time (arb)", fontsize=18)
    ax2.set_ylabel(f"Z-Projection of Spin Vector", fontsize=18)
    ax2.tick_params(axis='both', which='major', labelsize=16)
    ax2.set_ylim(-1, 1)
    ax2.set_xlim(0, data.Time[Total_No_of_data_points])
    '''
    
    BSfcs.Make_a_pretty_Bloch_sphere(ax1, linestyle, linewidth, ax2 = None)
    BSfcs.Plot_Bloch_trajectories(i, Signal_color, linewidth, ax1, arrowhead_size, data, drive_colour_x, drive_colour_z, Signal_Max_Y, Spin_colours, ax2)
    plt.savefig(f"{output_dir}/frame_{Frame_no}.png")  # Save each frame
    #plt.show()    
    plt.close()
    
    Frame_no += 1
    
filenames = [f"{output_dir}/frame_{index}.png" for index in range(Frame_no)]
images = [imageio.imread(filename) for filename in filenames]
imageio.mimsave("X Eigenstates.gif", images, duration=75)  # Adjust duration as needed
    
