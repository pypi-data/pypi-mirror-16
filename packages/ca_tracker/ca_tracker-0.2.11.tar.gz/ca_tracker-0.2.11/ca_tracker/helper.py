
import ca_tracker.idaf_io as iio
import ca_tracker.idaf_image_processing as iip
import numpy as np
import os
import ca_tracker
import skimage.morphology as morph
from skimage import io
import json

import logging
from logging.config import fileConfig


#fileConfig(os.path.dirname(ca_tracker.__file__) + '/config/logging_config.ini')
logger = logging.getLogger(os.path.basename(__file__))


def getExpNames(conf_data):
    names_singlechannel = iio.getFilelistFromDir(conf_data['data_locations']['imagefolder'], '_singlechannel', avoidpattern='.')
    names_rgb = iio.getFilelistFromDir(conf_data['data_locations']['imagefolder'], '_rgb', avoidpattern='.')

    names_s = [name.replace('_singlechannel', '') for name in names_singlechannel]
    names_r = [name.replace('_rgb', '') for name in names_rgb]
    names_s.sort()
    names_r.sort()

    #check if _rgb folders and _singlechannel folders are complete (match each other)
    if names_s != names_r:
        return None
    return names_s    



def readConfig(filename=None):
    if filename is None:    
        filename = 'ca_tracker/config/config.json'
    with open(filename) as data_file:
        conf_data = json.load(data_file)
    return conf_data    

def loadImage(path):
    im = loadTiff2PixelChannel(path)
    return np.squeeze(im)




def loadTiff2PixelChannel(channel_filename):
    '''
    reads a single tiff image and returns a PixelChannel
    '''
    
    absname = os.path.abspath(str(channel_filename))
    
    
    #logging.info("Loading '%s' with skimage...", absname)
    
    return io.imread(absname)




def loadVolume_inner(path, pattern):
    filenames_all = iio.getFilelistFromDir(path,pattern)
    
    #sort out filenames with dot in front (as made by mac finder)
    filenames = [name for name in filenames_all if name[0] !='.']

    filenames.sort()
    logger.debug('detected list of files: %s', filenames)
    

    name = filenames[0]
    im = loadImage(path+name)
    n_frames = len(filenames)
    n_y = im.shape[0]
    n_x = im.shape[1]

    vol = np.zeros([n_frames,n_y, n_x])
    logger.debug('vol_shape: %s', vol.shape) 
    
    for frame in range(n_frames):
        name = filenames[frame]
        vol[frame,:,:] = loadImage(path+name)

    return vol.astype('uint16') 





def loadVolume(path, module_name, channel):
    
    pattern = [module_name + '_t', 'c00' + str(channel), '.tif']

    return loadVolume_inner(path, pattern)

def loadTotalVolume(path, module_type, channel):
    module_names = getModuleNames(path, module_type=module_type)

    vol = loadVolume(path, module_names[0], channel)

    for name in module_names[1:]:
        akt_vol = loadVolume(path, name, channel)
        vol = np.concatenate((vol, akt_vol), axis=0)

    return vol  



def contoursFromMask(msk):
    labelmat = morph.label(msk)
    labelmat[labelmat==0] = np.max(labelmat.flatten())+1
    labelmat[msk==False]=0
    return iip.bwboundaries(labelmat)



def getModuleNames(path, module_type=None):
    pattern = ['_c00', '.tif']
    names = iio.getFilelistFromDir(path,pattern)
    for i in range(len(names)):
        names[i] = names[i][:4]
    
    module_names = np.unique(names)

    if module_type is None:
        return module_names

    return [k for k in module_names if module_type in k]


def getBoolmatForLabels(labelmat, labels):
    '''
    give a label matrix and a list of labels and get a boolean matrix with
    True where any of the labels is present
    ''' 
    boolmap = labelmat != labelmat
    for label in labels:
        tmp = labelmat==label
        boolmap = np.any(np.array([boolmap, tmp]), axis=0)
    return boolmap



def getBoundariesForLabels(labelmat, labels, with_labels=False):
    '''
    give a label matrix and a list of labels and get a list of boundary coordinates
    '''
    boolmat = getBoolmatForLabels(labelmat, labels)

    labelmat_clean = labelmat.copy()
    labelmat_clean[~boolmat] = 0
    
    return iip.bwboundaries(labelmat_clean, with_labels=with_labels)


def getCentroidsForLabels(labelmat, labels, with_labels=False):
    boolmat = getBoolmatForLabels(labelmat, labels)

    labelmat_clean = labelmat.copy()
    labelmat_clean[~boolmat] = 0

    labels_avail = np.unique(labelmat_clean)[1:]

    return getCentroids(labelmat_clean, with_labels=with_labels)


def getCentroidsAndBoundariesForLabels(labelmat, labels):
        bnd, labels_bn = getBoundariesForLabels(labelmat, labels, with_labels=True)
        cent, labels_cent = getCentroidsForLabels(labelmat, labels, with_labels=True)
        if labels_bn.tolist() == labels_cent.tolist():
            return {'boundaries': bnd, 'centroids' : cent, 'labels' : labels_bn}


def getCentroids(label_mat, with_labels=False):
    labels = getLabels(label_mat)
    xc = []
    yc = []
    for label in labels:
        coor = np.nonzero(label_mat == label)
        xc.append(np.mean(coor[0]))
        yc.append(np.mean(coor[1]))

    centroids  = np.array([xc, yc])
    
    if with_labels:
        return centroids.swapaxes(0,1), labels
    
    return centroids.swapaxes(0,1)  

def getLabels(label_mat):
    labels = np.unique(label_mat)
    return labels[1:]


def is_ca_module_filename(filename):
    return filename[1:5] == '_ca_'


def format_channel_suffix(channel_dict):
    return 'channel_ca_' + str(channel_dict['ca']) + '_sp_' + str(channel_dict['sp'])


def format_readout_channels(channels_ca, channels_sp):
    channel_dicts = \
        [{'ca' : channels_ca[i], 'sp' : channels_sp[i]} for i in range(len(channels_ca))]

    return channel_dicts


