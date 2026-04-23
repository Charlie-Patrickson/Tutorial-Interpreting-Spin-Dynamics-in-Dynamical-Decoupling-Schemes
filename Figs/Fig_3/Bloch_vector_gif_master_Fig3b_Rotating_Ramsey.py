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
arrowhead_size = 24
Signal_Max_Y = 0.75
drive_colour_z = "#E78C07"
drive_colour_x = "#CA2C20"
Signal_color = "#218D8C"
Spin_colours = ['k', 'dimgrey', 'grey', 'darkgrey', 'lightgrey']

data = [pd.read_csv("RotatingRamsey.csv")]
Total_No_of_data_points = 352

index = 0
Frame_no = 0

for i in range(0, Total_No_of_data_points, Skip_lines+1):

    fig = plt.figure(figsize=(20,8))
    ax1 = fig.add_axes([0.05, 0.1, 0.4, 0.8], projection='3d',computed_zorder=False)  # [left, bottom, width, height]
    
    ax2 = fig.add_axes([0.5, 0.2, 0.4, 0.45]) # [left, bottom, width, height]
    ax2.set_xlabel(f"Time (arb)", fontsize=22)
    ax2.set_ylabel(r"$S_z$", fontsize=22)
    ax2.tick_params(axis='both', which='major', labelsize=16)
    ax2.set_ylim([-1.25, 1.25])
    ax2.set_yticks([-1, -0.5, 0, 0.5, 1])
    ax2.set_xlim(0, data[0].Time[Total_No_of_data_points])
    
    ax3 = fig.add_axes([0.5, 0.65, 0.4, 0.2]) # [left, bottom, width, height]
    ax3.xaxis.set_label_position('top')
    ax3.xaxis.tick_top()
    ax3.set_xlabel(f"Time (arb)", fontsize=22)
    ax3.set_ylabel(r"$\Omega_x$", fontsize=22)
    ax3.tick_params(axis='both', which='major', labelsize=16)
    ax3.set_ylim(-3, 3)
    ax3.set_xlim(0, data[0].Time[Total_No_of_data_points])

    BSfcs.Make_a_pretty_Bloch_sphere(ax1, linestyle, linewidth, ax2 = None)
    BSfcs.Plot_Bloch_trajectories(i, Signal_color, linewidth, ax1, arrowhead_size, data, drive_colour_x, drive_colour_z, Signal_Max_Y, Spin_colours, ax2, ax3)
    plt.savefig(f"{output_dir}/frame_{Frame_no}.png")  # Save each frame
    #plt.show()    
    plt.close()
    
    Frame_no += 1
    
filenames = [f"{output_dir}/frame_{index}.png" for index in range(Frame_no)]
images = [imageio.imread(filename) for filename in filenames]
imageio.mimsave("RotatingRamsey.gif", images, duration=50)  # Adjust duration as needed
    
