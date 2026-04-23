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

Skip_lines = 4
linewidth = 2
linestyle = "solid"
arrowhead_size = 24
Signal_Max_Y = 0.75
drive_colour_z = "#E78C07"
drive_colour_x = "#CA2C20"
Signal_color = "#218D8C"

#data = pd.read_csv("RotatingRamsey.csv")
Noisy_data1 = pd.read_csv("Noisy Rotating Ramsey1.csv")
Noisy_data2 = pd.read_csv("Noisy Rotating Ramsey2.csv")
Noisy_data3 = pd.read_csv("Noisy Rotating Ramsey3.csv")
Noisy_data4 = pd.read_csv("Noisy Rotating Ramsey4.csv")
Noisy_data5 = pd.read_csv("Noisy Rotating Ramsey5.csv")
data = [Noisy_data1, Noisy_data2, Noisy_data3, Noisy_data4,  Noisy_data5][::-1]
#Spin_colours = ['k', 'dimgrey', 'grey', 'darkgrey', 'lightgrey'][::-1] #Grayscale
Spin_colours = ['#3A049A', '#A82296', '#D12E21', '#F57E1B', '#F5CD05'][::-1] #Plasma

Total_No_of_data_points = 2060

index = 0
Frame_no = 0

for i in range(0, Total_No_of_data_points, Skip_lines+1):
    
    fig = plt.figure(figsize=(32,8))
    ax1 = fig.add_subplot(131, projection='3d',computed_zorder=False)

    ax2 = fig.add_subplot(132)
    ax2.set_xlabel(f"Time (arb)", fontsize=18)
    ax2.set_ylabel(f"Z-Projection of Spin Vector", fontsize=18)
    ax2.tick_params(axis='both', which='major', labelsize=16)
    ax2.set_ylim(-1, 1)
    ax2.set_xlim(0, data[0].Time[Total_No_of_data_points])

    ax3 = fig.add_subplot(133)
    ax3.set_xlabel(f"Time (arb)", fontsize=18)
    ax3.set_ylabel(f"Z-Projection of Spin Vector", fontsize=18)
    ax3.tick_params(axis='both', which='major', labelsize=16)
    ax3.set_ylim(-1, 1)
    ax3.set_xlim(0, data[0].Time[Total_No_of_data_points])    

    BSfcs.Make_a_pretty_Bloch_sphere(ax1, linestyle, linewidth, ax2 = None)
    BSfcs.Plot_Bloch_trajectories(i, Signal_color, linewidth, ax1, arrowhead_size, data, drive_colour_x, drive_colour_z, Signal_Max_Y, Spin_colours, ax2, ax3)
    plt.savefig(f"{output_dir}/frame_{Frame_no}.png")  # Save each frame
    #plt.show()    
    plt.close()
    
    Frame_no += 1
    
filenames = [f"{output_dir}/frame_{index}.png" for index in range(Frame_no)]
images = [imageio.imread(filename) for filename in filenames]
imageio.mimsave("Noisy Rotating Ramsey.gif", images, duration=40)  # Adjust duration as needed
    
