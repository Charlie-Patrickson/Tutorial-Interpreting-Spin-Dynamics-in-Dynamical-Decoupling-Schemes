# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 14:36:28 2024

@author: cp728
"""

import numpy as np
import scipy
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
dot =  np.linalg.multi_dot

def Make_solid_outer_circle(Tilt_angle, ax, linewidth):
    
    Tilt_angle = (Tilt_angle/180)*np.pi
    
    phi = np.linspace(0, 2*np.pi, 100)    
    
    scale = 1.007
    
    x = scale*np.full_like(phi, 0) 
    y = scale*np.cos(phi)
    z = scale*np.sin(phi)
    
    Ry = np.array([[np.cos(Tilt_angle), 0, -np.sin(Tilt_angle)], [0, 1, 0], [np.sin(Tilt_angle), 0, np.cos(Tilt_angle)]])
    Rz = np.array([[np.cos(Tilt_angle), -np.sin(Tilt_angle), 0], [np.sin(Tilt_angle), np.cos(Tilt_angle), 0], [0, 0, 1]])
    
    vector = dot([Rz, Ry, [x, y, z]])
    
    ax.plot(vector[0], vector[1], vector[2], linestyle='solid', linewidth=linewidth, color='k')


def axis_dots(x, y, z, ax):    
    ax.text(x, y, z, " ", color = "grey", va="center", ha="center", fontsize= 'xx-small',
            bbox={"fc": "w", "alpha": 1, "boxstyle": "circle", "facecolor":"grey"})

def plot_circle(ax, plane, radius, linestyle='solid', linewidth=1, z_position=0, phi1 = 0, phi2=2*np.pi, colour = "grey"):
    theta = np.linspace(phi1, phi2, 100)
    if plane == 'XY':
        x = radius * np.cos(theta)
        y = radius * np.sin(theta)
        z = np.full_like(theta, z_position)
    elif plane == 'YZ':
        x = np.full_like(theta, z_position) 
        y = radius * np.cos(theta)
        z = radius * np.sin(theta)   
        
    elif plane == 'XZ':
        x = radius * np.cos(theta)
        y = np.full_like(theta, z_position)
        z = radius * np.sin(theta)

    ax.plot(x, y, z, linestyle=linestyle, linewidth=linewidth, color=colour)

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        super().__init__((0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))

        return np.min(zs)
    

def Make_a_pretty_Bloch_sphere(ax, linestyle, linewidth=1, Tilt_angle=18, ax2 = None):
    # Create Bloch sphere data points
    
    linestyle = (0, (8, 3))  # (on_off_seq)
    
    phi = np.linspace(0, 2 * np.pi, 100)
    theta = np.linspace(0, np.pi, 50)
    phi, theta = np.meshgrid(phi, theta)
    
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)
    
    # Plot small dots at the axes
    ax.scatter([0], [0], [0], color='black')
    
    axis_dots(0, 0, 1, ax)
    axis_dots(0, 0, -1, ax)
    axis_dots(0, 1, 0, ax)
    axis_dots(0, -1, 0, ax)
    axis_dots(1, 0, 0, ax)
    axis_dots(-1, 0, 0, ax)
    
    # Plot circles on the XY, YZ, and XZ planes at y=0, z=0, and x=0, respectively
    plot_circle(ax, 'XY', radius=1, linestyle=linestyle, linewidth=linewidth)  # Circle on XY plane (y=0)
    plot_circle(ax, 'YZ', radius=1, linestyle=linestyle, linewidth=linewidth)  # Circle on YZ plane (z=0)
    plot_circle(ax, 'XZ', radius=1, linestyle=linestyle, linewidth=linewidth)  # Circle on XZ plane (x=0)
    
    Make_solid_outer_circle(Tilt_angle, ax, linewidth)
    
    ax.view_init(Tilt_angle, Tilt_angle)
    ax.axis('off')
    ax.set_box_aspect([1, 1, 1])
    
    limit = 0.62
    ax.axes.set_xlim3d(left=-limit, right =limit)
    ax.axes.set_ylim3d(bottom=-limit, top=limit) 
    ax.axes.set_zlim3d(bottom=-limit, top=limit) 
    
    
def Plot_Bloch_trajectories(i, Signal_color, linewidth, ax, arrowhead_size, data, drive_colour_x, drive_colour_z, Signal_Max_Y, spin_colours='k', ax2 = None):
    
    index = 0
    
    for df in data:
    
        ''' Add Spin Vectors'''
        
        time = df.Time
        
        x = df.Sx
        y = df.Sy
        z = df.Sz
        
        ax.plot(x[0:i+1], y[0:i+1], z[0:i+1], linewidth=linewidth, color = spin_colours[index])
        ax.set_title(f"t = {time[i]:.3f}")
        
        arrow_prop_dict = dict(arrowstyle='-|>', linewidth = linewidth*2, mutation_scale=arrowhead_size, color = spin_colours[index], shrinkA=0, shrinkB=0)
        a = Arrow3D([0, x[i]], [0, y[i]], [0, z[i]], **arrow_prop_dict)
        ax.add_artist(a)
        
        if ax2:
            ax2.plot(time[0:i], z[0:i], color = spin_colours[i])

        ''' Add drive '''
    
        if "Hx" in df.columns:
            
            drive_x = df.Hx
            drive_y = df.Hy
            drive_z = df.Hz
            
            if np.any(np.abs(drive_x)) > 0:
                drive_x = 0.6*drive_x/np.max(drive_x)
                
            if np.any(np.abs(drive_y > 0)):
                drive_y = 0.6*drive_y/np.max(drive_y)
                
            if np.any(np.abs(drive_z > 0)):
                drive_z = 0.6*drive_z/np.max(drive_z)
    
            arrow_prop_dict = dict(arrowstyle='-|>', linewidth = linewidth*2, mutation_scale=arrowhead_size, color=drive_colour_x, shrinkA=0, shrinkB=0)
            a = Arrow3D([0, drive_x[i]], [0, 0], [0, 0], **arrow_prop_dict)
            ax.add_artist(a)
            
            arrow_prop_dict = dict(arrowstyle='-|>', linewidth = linewidth*2, mutation_scale=arrowhead_size, color='k', shrinkA=0, shrinkB=0)
            a = Arrow3D([0, 0], [0, drive_y[i]], [0, 0], **arrow_prop_dict)
            ax.add_artist(a)
            
            arrow_prop_dict = dict(arrowstyle='-|>', linewidth = linewidth*2, mutation_scale=arrowhead_size, color=drive_colour_z, shrinkA=0, shrinkB=0)
            a = Arrow3D([0, 0], [0, 0], [0, drive_z[i]], **arrow_prop_dict)
            ax.add_artist(a)
            
        index =+1

    '''Add signal waveform:'''
    
    if "Signal_x" in df.columns:
        
        signal_x = np.array(df.Signal_x/(np.pi))
        signal_y = np.array(df.Signal_y/(np.pi))
        signal_z = np.array(df.Signal_z/(np.pi))
        
        # Plot a sine wave in the XY plane along the x-axis
    
        if i < 200:
    
            signal_x = signal_x[0:i]
            signal_y = signal_y[0:i]
            signal_z = signal_z[0:i]
            
        else:
            
            signal_x = signal_x[i - 200:i]
            signal_y = signal_y[i - 200:i]
            signal_z = signal_z[i - 200:i]
        
        ax.plot(signal_x, signal_y, signal_z, color = Signal_color, linewidth = linewidth*2)
        
        try:
            arrow_prop_dict = dict(arrowstyle='-|>', linewidth = linewidth*2, mutation_scale=arrowhead_size, color=Signal_color, shrinkA=0, shrinkB=0)
            a = Arrow3D([0, signal_x[0]], [0, 0], [0, 0], **arrow_prop_dict)
            ax.add_artist(a)
            
        except:
            pass



    
