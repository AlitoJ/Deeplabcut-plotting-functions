# Deeplabcut-plotting-functions
When using the AlexEMG/Deeplabcut toolbox for plotting the histogram of likelihood, 
the large amount of frames and several bodyparts overlap in one figure. 
This makes the legibility pretty low. 
This python file helps separate the bodyparts and plot the histogram of likelihood-count (cumulative&normed are plotted as well).

Histogram-plot.py is the new plotting function. For looking-up convenience, I upload the auxiliaryfunctions.py from AlexEMG/DEEPLABCUT files because of the importing issues. You can search for more details through AlexEMG's pages.https://github.com/AlexEMG/DeepLabCut

These are the original figures plotted by the Deeplabcut Toolbox, which are hist,plot,trajectory,plot-likelihood in order

![test](https://github.com/AlitoJ/Deeplabcut-plotting-functions/blob/master/img/hist.png) 
![test](https://github.com/AlitoJ/Deeplabcut-plotting-functions/blob/master/img/plot.png)
![test](https://github.com/AlitoJ/Deeplabcut-plotting-functions/blob/master/img/trajectory.png)
![test](https://github.com/AlitoJ/Deeplabcut-plotting-functions/blob/master/img/plot-likelihood.png)

Utilizing the Histogram-plot.py you are able to plot new figures like these:

![test](https://github.com/AlitoJ/Deeplabcut-plotting-functions/blob/master/img/leftear-hist.png)
![test](https://github.com/AlitoJ/Deeplabcut-plotting-functions/blob/master/img/rightear-hist.png)
![test](https://github.com/AlitoJ/Deeplabcut-plotting-functions/blob/master/img/snout-hist.png)
![test](https://github.com/AlitoJ/Deeplabcut-plotting-functions/blob/master/img/tail-hist.png)

The normed&cumulative frenquency histograms are also available
![test](https://github.com/AlitoJ/Deeplabcut-plotting-functions/blob/master/img/leftear-hist-cumulative.png)
![test](https://github.com/AlitoJ/Deeplabcut-plotting-functions/blob/master/img/rightear-hist-cumulative.png)
![test](https://github.com/AlitoJ/Deeplabcut-plotting-functions/blob/master/img/snout-hist-cumulative.png)
![test](https://github.com/AlitoJ/Deeplabcut-plotting-functions/blob/master/img/tail-hist-cumulative.png)
