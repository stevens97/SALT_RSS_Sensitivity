# SALT_RSS_Sensitivity
Create a sensitivity file for a FITS file image of a standard star processed by the Southern African Large Telescope (SALT) Robert Stobie Spectrograph (RSS).

What this program does:
========================================

The SALT RSS data reduction procedure is well documented.

See the data reduction procedure here:
http://mips.as.arizona.edu/~khainline/salt_redux.html

Also see the data reduction FAQ:
https://astronomers.salt.ac.za/data/data-reduction-faq/

This program creates a ''sensitivity file'' from the FITS file of a standard star.
This file can later be used by IRAF to apply flux calibration to the FITS file of another astronomical source.

Prerequisites for using this program:
========================================

This program requires a programming environment with Python 3.6 installed.
With the following external libraries:
- PyRAF, 
- Astropy
- see: https://faculty1.coloradocollege.edu/~sburns/courses/18-19/pc362/Anaconda_IRAF_install.html for installation instructions.

