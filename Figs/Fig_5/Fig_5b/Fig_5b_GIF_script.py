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
from matplotlib.gridspec import GridSpec, GridSpecFromSubplotSpec

from matplotlib import rcParams
plt.rcParams['mathtext.fontset'] = 'dejavuserif'
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.sans-serif'] = ['Cambria math', 'sans-serif']

output_dir = "frames"
os.makedirs(output_dir, exist_ok=True)  # Only creates it if it doesn't already exist

Skip_lines = 1
linewidth = 2
linestyle = "solid"
arrowhead_size = 24
Signal_Max_Y = 0.75
drive_colour_z = "#42A2AC"
drive_colour_x = "#455DC3"
Signal_color = "#218D8C"

data = pd.read_csv("Fig_5b_SimData_1.csv")
Noisy_data = pd.read_csv("Fig_5b_SimData_2.csv")
Detuned_Rabi = pd.read_csv("Fig_5b_SimData_3.csv")
Perfect_Rabi = pd.read_csv("Fig_5b_SimData_4.csv")
data = [data, Noisy_data, Detuned_Rabi, Perfect_Rabi]
Spin_colours = ['#2406A2', '#A01B9B', '#F1814C', '#FAD524', 'lightgrey']
Detunings = [r"$CCD ~(\omega = \omega_0, \Omega \neq \omega_m)$", r"$CCD ~(\omega \neq \omega_0, \Omega = \omega_m)$", r"$Detuned~Rabi$", r"$Target~Rabi$"]

Total_No_of_data_points = 333

index = 0
Frame_no = 0

for i in range(0, Total_No_of_data_points, Skip_lines):
    
    
    fig = plt.figure(figsize=(32, 8))
    
    # Outer grid: 3 columns
    gs = GridSpec(1, 3, figure=fig)
    
    # ax1 unchanged
    ax1 = fig.add_subplot(gs[0], projection='3d', computed_zorder=False)
    
    # Split ax2 column into two vertically
    gs2 = GridSpecFromSubplotSpec(2, 1, subplot_spec=gs[1], hspace=0.05, height_ratios=[1, 3])
    ax2a = fig.add_subplot(gs2[0])
    ax2b = fig.add_subplot(gs2[1])
    
    '''
    # Split ax3 column into two vertically
    gs3 = GridSpecFromSubplotSpec(2, 1, subplot_spec=gs[2], hspace=0.05, height_ratios=[1, 3])
    ax3a = fig.add_subplot(gs3[0])
    ax3b = fig.add_subplot(gs3[1])
    '''
    
    # Formatting ax2a / ax2b
    ax2a.set_ylabel(r"$H_{CCD, y}^{\prime}$", fontsize=18)
    ax2a.tick_params(axis='both', which='major', labelsize=16)
    ax2a.set_ylim(-5, 5)
    ax2a.set_xlim(0, data[0].Time[Total_No_of_data_points])
    
    ax2b.set_ylabel(r"$S_z^{\prime}$", fontsize=18)
    ax2b.tick_params(axis='both', which='major', labelsize=16)
    ax2b.set_ylim(-1.1, 1.1)
    ax2b.set_xlim(0, data[0].Time[Total_No_of_data_points])
    
    ax2a.set_xticklabels([])  # hide x ticks on top plot
    ax2b.set_xlabel("Time (arb)", fontsize=18)
    '''
    # Formatting ax3a / ax3b
    ax3a.set_ylabel(r"$H_{CCD, y}^{\prime}$", fontsize=18)
    ax3a.tick_params(axis='both', which='major', labelsize=16)
    ax3a.set_ylim(-5, 5)
    ax3a.set_xlim(0, data[0].Time[Total_No_of_data_points])
    
    ax3b.set_ylabel(r"$S_x^{\prime}$", fontsize=18)
    ax3b.tick_params(axis='both', which='major', labelsize=16)
    ax3b.set_ylim(-1.1, 1.1)
    ax3b.set_xlim(0, data[0].Time[Total_No_of_data_points])
    
    ax3a.set_xticklabels([])  # hide x ticks on top plot
    ax3b.set_xlabel("Time (arb)", fontsize=18)
    '''
    
    last_i = range(0, Total_No_of_data_points, Skip_lines+1)[-1]
    
    BSfcs.Make_a_pretty_Bloch_sphere(ax1, linestyle, linewidth, ax2=None)
    BSfcs.Plot_Bloch_trajectories(i, Signal_color, linewidth, ax1, arrowhead_size, data,
                                   drive_colour_x, drive_colour_z, Signal_Max_Y, Detunings, Spin_colours,
                                   ax2b, ax2a, ax3b=None, ax3a=None)  # or whichever axes your function expects
    
    plt.savefig(f"{output_dir}/frame_{Frame_no}.png")
    plt.close()
        
    Frame_no += 1
    
'''
filenames = [f"{output_dir}/frame_{index}.png" for index in range(Frame_no)]
images = [imageio.imread(filename) for filename in filenames]
imageio.mimsave("Fig_4b.gif", images, duration=75)  # Adjust duration as needed
'''
with imageio.get_writer("Fig_5b.gif", mode="I", duration=110) as writer:
    for n in range(Frame_no):
        img = imageio.imread(f"{output_dir}/frame_{n}.png")
        writer.append_data(img)  
