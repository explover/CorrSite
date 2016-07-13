#Graph_module
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.ticker
from pylab import *
import numpy as np
from scipy.stats import gaussian_kde


class build:
	def dist_corr(self,fig11=None, fig12=None):
		
		#Defining variables
		data=[0,0]
		data[0] = fig11
		data[1] = fig12		
		
		
		dens = [gaussian_kde(data[0]), gaussian_kde(data[1])]
		dens[0].covariance_factor = lambda : .125
		dens[0]._compute_covariance()
		dens[1].covariance_factor = lambda : .125
		dens[1]._compute_covariance()
		x = np.linspace(-1.,1.,200)		
		
		figure()
		title('Distribution of correlations')		
		xlabel('correlation coefficient')
		ylabel('density')		
		plot(x, dens[0](x), antialiased=True, c='r')
		plot(x, dens[1](x), antialiased=True, c='b')
		savefig('/home/roman/real.png')
	def auto_corr(self,fig21=None, fig22=None):
		
		data=[0,0]
		data[0] = fig11
		data[1] = fig12		
		
		
		dens = [gaussian_kde(data[0]), gaussian_kde(data[1])]
		dens[0].covariance_factor = lambda : .125
		dens[0]._compute_covariance()
		dens[1].covariance_factor = lambda : .125
		dens[1]._compute_covariance()
		x = np.linspace(-100,100,2000)		
		
		figure()
		title('Correlation function')		
		xlabel('Distance (kb)')
		ylabel('%')		
		plot(x, dens[0](x), antialiased=True, c='r')
		plot(x, dens[1](x), antialiased=True, c='b')
		savefig('/home/roman/real.png')
	def box_plot(box_plot):
		chrom=list(box_plot.keys())
		chrom.sort()
		data=[]
		for i in chrom:
			data.append(box_plot[i])
		fig=figure()
		axes=figure.add_subplot(1,1,1)	
		formatter=matplotlib.ticker.FixedFormatter(chrom)
		axes.xaxis.set_major_formatter(formatter)
		
		plt.boxplot(data)
		axes.grid()
		savefig('boxplot.png')

	def __init__(self, fig11=None, fig12=None, fig21=None, fig22=None, box_plot=None):
		self.dist_corr(fig11, fig12)
	
