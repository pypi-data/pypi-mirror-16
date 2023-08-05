import pickle
import helper as h
import numpy as np
import pandas as pd 
from skimage.feature import hessian_matrix_det
import os
import logging
from logging.config import fileConfig

#fileConfig('ca_tracker/config/logging_config.ini')
logger = logging.getLogger(os.path.basename(__file__))

def computeFeaturesForLabel(vol_s, labelvol, label, median_of_vol):
	n_frames = labelvol.shape[0]
	tb = pd.DataFrame(columns=['filename', 'module_nr', 'module_type'\
				, 'label','frame', 'time_abs', 'area', 'av_s', 'cv_s'])
	
	

	for frame in range(n_frames):
		im_s = vol_s[frame,:,:]
		#im_bg_filtered = im_s - median(im_s, disk(config.median_filter_size))
		im_label = labelvol[frame,:,:]
		pixels = im_s[im_label==label]

		row = {}
		row['label'] = label
		
		row['frame'] = frame
		row['area'] = len(pixels)

		#if object is not existing in actual frame
		if row['area'] == 0:
			row['area'] = np.nan
			row['av_s'] = np.nan
			row['cv_s'] = np.nan
			row['rel_max_s'] = np.nan
		else:	
			row['av_s'] = np.mean(pixels)
			row['cv_s'] = np.std(pixels)#/row['av_s']
			row['rel_max_s'] = np.max(pixels)/median_of_vol
		tb = tb.append(row, ignore_index=True)
	return tb	






#exp_filenames = ['75ms_7p5_1', '75ms_7p5_2', '50ms_7p5_1', '50ms_7p5_2']
exp_filenames = ['50ms_7p5_1']



def compute_features(exp_filename, config):

	resultsfolder = config['data_locations']['resultsfolder']
	imagefolder = config['data_locations']['imagefolder']
	speck_channel =  config['channel_mapping']['speck_channel_sp']

	#import tracking data table
	t_dat = pickle.load(open(resultsfolder + exp_filename + '_trackdata.pickle', 'rb'))

	#import 3d labelmatrix
	labelvol = t_dat['track_labelvol']
	#import speck images
	vol_s = h.loadTotalVolume(imagefolder + exp_filename + '_singlechannel/', 'sp', speck_channel)
	
	hessian_vol = vol_s.copy()

	for i in range(vol_s.shape[0]):
		#hessian_vol[:,:,i] = flt.gaussian_filter(hessian_matrix_det(vol_s[:,:,i], 3.1), [0.2, 0.2])
		
		#compute hessian determinant to find specking cells 
		hessian_vol[:,:,i] = hessian_matrix_det(vol_s[:,:,i], 3.1)
	#compute median for normalization
	median_of_hessian = np.median(hessian_vol.flatten()) 	
	
	#import table with abolute times	
	timetable = pd.read_csv(resultsfolder + exp_filename + '_timetable.csv')


	n_frames = labelvol.shape[0]
	labels = np.unique(labelvol.flatten())[1:]


	tb = pd.DataFrame()
	logger.info('start compute features of %s for %s labels', exp_filename, labels[-1])
	for label in labels:
		
		tb_forlabel = computeFeaturesForLabel(hessian_vol, labelvol, label, median_of_hessian)
		tb_forlabel['time_abs'] = timetable[timetable['module_type'] == 'sp']['time_abs'].tolist()
		tb_forlabel['module_type'] = timetable[timetable['module_type'] == 'sp']['module_type'].tolist()
		tb_forlabel['module_nr'] = timetable[timetable['module_type'] == 'sp']['module_nr'].tolist()
		tb_forlabel['filename'] = timetable[timetable['module_type'] == 'sp']['filename'].tolist()
		tb = tb.append(tb_forlabel)
		savename = exp_filename + '_features.csv'
	logger.info('computing features of %s finished', exp_filename)
	logger.info('write feature table for %s to %s', exp_filename, savename)	
	tb.to_csv(resultsfolder + savename)







