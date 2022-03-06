'''
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

SALT RSS Sensitivity File Creator

This program creates a sensitivity file for a given standard star that has been
reduced by the SALT RSS pipeline.

The target FITS file is typically a 2D flux spectrum of the standard star.

The SALT RSS Data Reduction procedure is described in:
http://mips.as.arizona.edu/~khainline/salt_redux.html

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''

'''
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Import Libraries
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''

import os  # For bash commands
from pyraf import iraf  # For IRAF commands in Python
import astropy.io.fits as fits  # For FITS file handling

'''
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Load IRAF Libraries
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''

iraf.noao()
iraf.noao.onedspec()

'''
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Create Standard File for Standard Star
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''


def standard(star):
    '''

    Creates a ``standard'' file from the standard star FITS file. This is an intermediary file required to create the ``sensitivity file'' later.

    :param star [String]: Filename of the standard star FITS file.

    :return: standard [String]: Filename of the standard FITS file to be created.
    '''

    # Set name of standard file
    standard = 'std_{}'.format(star)

    # Open FITS file of standard star
    hdu = fits.open(star)
    hdu[0].verify('fix')
    hdr = hdu[0].header

    star_name = hdr['OBJECT']
    AIRMASS = hdr['AIRMASS']
    EXPTIME = hdr['EXPTIME']

    # Create standard star
    iraf.noao.onedspec.standard(input=star, output=standard, samestar='yes', beam_switch='no', apertures='',
                                bandwidth='INDEF', bandsep='INDEF', fnuzero=3.68e-20,
                                extinction='onedstds$ctioextinct.dat',
                                caldir='/home/user/Desktop/SALT/std_dat/', observatory='saao', interact='no',
                                graphics='stdgraph', cursor='', star_name=star_name, airmass=AIRMASS, exptime=EXPTIME,
                                answer='yes', mode='ql')

    return standard


'''
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Create Sensitivity File for Standard Star
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''


def sensitivity(star, standard):
    '''

    Create a ``sensitivity'' file from the standard FITS file. This file is needed for future flux calibration with IRAF.

    :param star [String]: Filename of the standard star FITS file.
    :param: standard [String]: Filename of the standard FITS file.

    :return: None
    '''

    # Set name of sensitivity file
    sens = 'sens_{}'.format(star)

    # Create sensitivity file
    iraf.noao.onedspec.sensfunc(standards=standard, sensitivity=sens, ignoreaps='Yes', logfile='logfile',
                                newextinction='extinct.dat', observatory='saao',
                                function='spline3', order=5, interactive='No', graphs='sr', marks='plus cross box',
                                colors='2 1 3 4', cursor='',
                                device='stdgraph', answer='yes', mode='ql')

    return None


'''
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Run Program
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''

print(
    '\n--------------------------------------\nSALT RSS Sensitivity File Creator\n--------------------------------------\n')

# Set file path of data.
path = raw_input('\nEnter file path of the directory that contains the FITS file:  ')
# Change filepath
os.chdir(path)

# Get name of star
star = raw_input('\nEnter file name (with extension) of the standard star FITS file:  ')

# Create Standard File
standard = standard(star)

# Create Sens File
sensitivity(star, standard)
