import os.path
from pathlib import Path
import argparse
from deeplabcut.utils import auxiliaryfunctions
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

#1.read the data first
def read_the_data(video,cfg,scorer):
    videofolder = str(Path(video).parents[0])
    dataname = str(Path(video).stem) + scorer + '.h5'
    Dataframe = pd.read_hdf(os.path.join(videofolder,dataname))
    return Dataframe

#2.count the number then plot
def plot_histogram(data,cfg,bodyparts,scorer,tmpfolder):
    colors = plt.get_cmap(lut=len(bodyparts),name = cfg['colormap'])
    #extract the value of likelihood
    for bpindex,bp in enumerate(bodyparts):
        Index=data[scorer][bp]['likelihood'].values
        #plot the histogram of likelihood-count of each bodypart
        plt.hist(Index, bins = 20, color = colors(bpindex))
        sm = plt.cm.ScalarMappable(cmap=plt.get_cmap(cfg['colormap']), norm=plt.Normalize(vmin=0, vmax=len(bodyparts)-1))
        sm._A = []
        cbar = plt.colorbar(sm,ticks=range(len(bodyparts)))
        cbar.set_ticklabels(bodyparts)
        plt.xlabel('Likelihood')
        plt.ylabel('Count')
        plt.title(bp)
        plt.savefig(tmpfolder+"/{}-hist.png".format(bp))
        plt.clf()

#3.Plot the cumulative frequency histogram
def plot_cumulative_histogram(data,cfg,bodyparts,scorer,tmpfolder):
    colors = plt.get_cmap(lut=len(bodyparts),name = cfg['colormap'])
    #extract the value of likelihood
    for bpindex,bp in enumerate(bodyparts):
        Index=data[scorer][bp]['likelihood'].values
        #plot the histogram of cumulative frequency distribution of each bodypart
        plt.hist(Index, bins = 20,normed=True,cumulative=True, color = colors(bpindex))
        sm = plt.cm.ScalarMappable(cmap=plt.get_cmap(cfg['colormap']), norm=plt.Normalize(vmin=0, vmax=len(bodyparts)-1))
        sm._A = []
        cbar = plt.colorbar(sm,ticks=range(len(bodyparts)))
        cbar.set_ticklabels(bodyparts)
        plt.xlabel('Likelihood')
        plt.ylabel('Cumulative frequency distribution')
        plt.title(bp)
        plt.savefig(tmpfolder+"/{}-cumulative-2095.png".format(bp))
        plt.clf()        

if __name__=='__main__':
        #type the correct address of yours
    configname = 'full path of the config.yaml'
    video_path = 'full path of the videos'
    savefolder = 'full path of the file you would like to save figures in'

    cfg = auxiliaryfunctions.read_config(configname) 
    trainFraction = cfg['TrainingFraction'][0]
    bodyparts2plot = cfg['bodyparts']
    colors = plt.get_cmap(lut=len(bodyparts2plot), name=cfg['colormap'])
    DLCscorer = auxiliaryfunctions.GetScorerName(cfg,1,trainFraction)

    DF = read_the_data(video=video_path,cfg=cfg,scorer=DLCscorer)
    plot_histogram(data=DF,cfg=cfg,bodyparts=bodyparts2plot,scorer=DLCscorer,tmpfolder=savefolder)
    plot_cumulative_histogram(data=DF,cfg=cfg,bodyparts=bodyparts2plot,scorer=DLCscorer,tmpfolder=savefolder)

