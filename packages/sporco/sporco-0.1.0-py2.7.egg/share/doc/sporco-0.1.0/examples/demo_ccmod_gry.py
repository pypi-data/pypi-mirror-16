#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Copyright (C) 2015-2016 by Brendt Wohlberg <brendt@ieee.org>
# All rights reserved. BSD 3-clause License.
# This file is part of the SPORCO package. Details of the copyright
# and user license can be found in the 'LICENSE.txt' file distributed
# with the package.

"""Basic ccmod.ConvCnstrMOD usage example (greyscale images)"""

from __future__ import print_function
from builtins import input
from builtins import range

import numpy as np
from scipy.ndimage.interpolation import zoom
import matplotlib.pyplot as plt

from sporco.admm import cbpdn
from sporco.admm import ccmod
from sporco import util


# Training images
exim = util.ExampleImages(scaled=True)
img1 = exim.image('lena.grey')
img2 = exim.image('barbara.grey')
img3 = exim.image('kiel.grey')
img4 = util.rgb2gray(exim.image('mandrill'))
img5 = exim.image('man.grey')[100:612, 100:612]


# Reduce images size to speed up demo script
S1 = zoom(img1, 0.5)
S2 = zoom(img2, 0.5)
S3 = zoom(img3, 0.5)
S4 = zoom(img4, 0.5)
S5 = zoom(img5, 0.5)
S = np.dstack((S1,S2,S3,S4,S5))


# Highpass filter test images
npd = 16
fltlmbd = 5
sl, sh = util.tikhonov_filter(S, fltlmbd, npd)


# Load initial dictionary
D0 = util.convdicts()['G:12x12x36']


# Compute sparse representation on current dictionary
lmbda = 0.05
opt = cbpdn.ConvBPDN.Options({'Verbose' : True, 'MaxMainIter' : 200,
                     'HighMemSolve' : True})
b = cbpdn.ConvBPDN(D0, sh, lmbda, opt)
b.solve()


# Update dictionary for training set sh
opt = ccmod.ConvCnstrMOD.Options({'Verbose' : True, 'MaxMainIter' : 100,
                                  'rho' : 5.0})
c = ccmod.ConvCnstrMOD(b.Y, sh, D0.shape, opt)
c.solve()
print("ConvCnstrMOD solve time: %.2fs" % c.runtime)
D1 = c.getdict().squeeze()


# Display dictionaries
fig1 = plt.figure(1, figsize=(14,7))
plt.subplot(1,2,1)
util.imview(util.tiledict(D0), fgrf=fig1, title='D0')
plt.subplot(1,2,2)
util.imview(util.tiledict(D1), fgrf=fig1, title='D1')
fig1.show()


# Plot functional value, residuals, and rho
its = c.getitstat()
fig2 = plt.figure(2, figsize=(21,7))
plt.subplot(1,3,1)
util.plot(its.DFid, fgrf=fig2, ptyp='semilogy', xlbl='Iterations',
          ylbl='Functional')
plt.subplot(1,3,2)
util.plot(np.vstack((its.PrimalRsdl, its.DualRsdl)).T, fgrf=fig2,
          ptyp='semilogy', xlbl='Iterations', ylbl='Residual',
          lgnd=['Primal', 'Dual']);
plt.subplot(1,3,3)
util.plot(its.Rho, fgrf=fig2, xlbl='Iterations', ylbl='Penalty Parameter')
fig2.show()


# Wait for enter on keyboard
input()
