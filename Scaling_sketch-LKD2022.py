#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt # matplotlib shorthand
import matplotlib.ticker as mtick
import sys # python system library
import numpy as np # numerical python library
import math # python math library
import glob
from matplotlib import cm
#import scipy
#from scipy import ndimage
#from PIL import Image


# Below are figure parameters you can tweak for your plots:


ff = 2
space         = ff*0.07
nb_lines      = ff*1
fig_width_pt  = 246.
inches_per_pt = 1./72.
golden_mean   = .66
fig_width     = fig_width_pt*inches_per_pt
fig_height    = (fig_width*golden_mean)+space
fig_size      = [ff*fig_width, ff*fig_height]
# Plot parameters
#plt.rcParams['figure.figsize'] = (7,5)
#plt.rcParams['figure.dpi'] = 150
#plt.rcParams["font.family"] = "Serif"
#plt.rcParams["font.size"] = 22
#params = {'mathtext.default': 'regular' }
params = {'font.family': "Serif",
        'legend.fontsize': ff*13,
          'axes.linewidth': ff*5e-1,
          'axes.labelsize': ff*15,
          #'text.fontsize': ff*4,
          'xtick.labelsize': ff*7,
          'ytick.labelsize': ff*7,
          'text.usetex': True,
          'figure.figsize': fig_size}
plt.rcParams.update(params)


# Create the plotting object. Note using subplots allows for easy expansion into multi plots.

fig, axs = plt.subplots(1,1,figsize=fig_size)


# == Basis for the harmonic trap particle sketch

#axs[0].set_xlim(0.0,1)
#axs[0][0].spines['top'].set_visible(False)
#axs[0][0].spines['right'].set_visible(False)
#axs.xaxis.set_visible(False)
axs.spines['right'].set_visible(False)
axs.spines['top'].set_visible(False)
#axs.axis('off')
axs.set_xticks([])
axs.set_yticks([])
axs.set(xlabel='Protocol duration',ylabel='Dissipation')
#axs[i].yaxis.set_major_formatter(mtick.FormatStrFormatter('%.0e'))
#axs[0][0].xaxis.set_major_locator(mtick.MultipleLocator(0.2))
#axs[0][0].xaxis.set_minor_locator(mtick.MultipleLocator(0.1))
#axs[0][0].yaxis.set_major_locator(mtick.AutoLocator())
#axs[0][0].yaxis.set_minor_locator(mtick.AutoLocator())

axs.tick_params(which='both',direction='in',left=False,right=False,top=False,bottom=False)
#axs[0][0].tick_params(which='major',direction='in',right=True,top=True)
#axs[0][0].tick_params(which='minor',direction='in',right=True,top=True)

#x[i] = [(xval / x[i][-1]) for xval in x[i] ]

axs.set_xlim(0.0,4)
axs.set_ylim(0.,3)

x= np.arange(0.01,10.0,0.01)
y= [0.5/i for i in x]
axs.plot(x,y,c='black',alpha=0.75,linewidth=ff*2,label='Passive')
x= np.arange(0.01,10.0,0.01)
y= [0.5/i + 0.5*i for i in x]
axs.plot(x,y,c='blue',alpha=0.75,linewidth=ff*2,label='Active')
axs.legend(frameon=False)

axs.vlines(1,0,1,colors='blue',ls='--')

axs.plot(1, 0, ">k", markersize=12,transform=axs.get_yaxis_transform(), clip_on=False)
axs.plot(0, 1, "^k", markersize=12,transform=axs.get_xaxis_transform(), clip_on=False)

#axs.text(-0.5, 1.5,r"$\phi(r)= \frac{1}{2} \alpha r^2$",size=ff*20)


# END PLOTTING THINGS
fig.tight_layout(pad=0.5)
plt.savefig('./Example-matplotlib-sketch.pdf')






