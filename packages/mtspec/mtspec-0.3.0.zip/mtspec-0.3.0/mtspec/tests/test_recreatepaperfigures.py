#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This test case will create figures of Prieto et al. (2008) for a visual
comparison to see whether or not the wrapper works.

Currently produces figure 1, figure 2 and figure 3.

References:
    * Prieto G, Parker R, Vernon III F. A Fortran 90 library for multitaper
      spectrum analysis. Computers & Geosciences. 2009;35(8):1701-1710.

:copyright:
    Lion Krischer (krischer@geophysik.uni-muenchen.de) and
    Moritz Beyreuther, 2010-2015
:license:
    GNU General Public License, Version 3
    (http://www.gnu.org/copyleft/gpl.html)
"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import os
import time
import unittest

import matplotlib.pylab as plt

from ..multitaper import mtspec, sine_psd
from ..util import _load_mtdata


plt.switch_backend("Agg")


class RecreateFigures(unittest.TestCase):
    """
    Test suite for recreating the figure 1, 2 and 3 of Prieto et al. 2008

    The test just recreates the figures and checks that something is
    created. The content is not verfied/controlled --- this should be
    covered by the test case test_multitaper.py
    """

    def setUp(self):
        self.outpath = os.path.join(os.path.dirname(__file__), 'output')

    def test_figure1(self):
        """
        Recreate Figure 1
        """
        data = _load_mtdata('v22_174_series.dat.gz')

        spec, freq, jackknife, _, _ = mtspec(
            data, 4930., 3.5, number_of_tapers=5, nfft=312, statistics=True)

        fig = plt.figure()
        ax1 = fig.add_subplot(2, 1, 1)
        ax1.plot(data, color='black')
        ax1.set_xlim(0, len(data))

        ax2 = fig.add_subplot(2, 1, 2)
        ax2.set_yscale('log')
        ax2.plot(freq, spec, color='black')
        try:
            ax2.fill_between(freq, jackknife[:, 0], jackknife[:, 1],
                             color='grey')
        except:
            ax2.plot(freq, jackknife[:, 0], '--', color='red')
            ax2.plot(freq, jackknife[:, 1], '--', color='red')
        ax2.set_xlim(freq[0], freq[-1])

        outfile = os.path.join(self.outpath, 'fig1.pdf')
        fig.savefig(outfile)
        stat = os.stat(outfile)
        self.assertTrue(abs(stat.st_mtime - time.time()) < 3)

    def test_figure2(self):
        """
        Recreate Figure 2
        """
        data = _load_mtdata('v22_174_series.dat.gz')
        spec, freq, jackknife, fstatistics, _ = mtspec(
            data, 4930., 3.5, number_of_tapers=5, nfft=312, statistics=True,
            rshape=0, fcrit=0.9)

        fig = plt.figure()
        ax1 = fig.add_subplot(2, 1, 1)
        ax1.plot(freq, fstatistics, color='black')
        ax1.set_xlim(freq[0], freq[-1])

        ax2 = fig.add_subplot(2, 1, 2)
        ax2.set_yscale('log')
        ax2.plot(freq, spec, color='black')
        ax2.set_xlim(freq[0], freq[-1])

        outfile = os.path.join(self.outpath, 'fig2.pdf')
        fig.savefig(outfile)
        stat = os.stat(outfile)
        self.assertTrue(abs(stat.st_mtime - time.time()) < 3)

    def test_figure3(self):
        """
        Recreate Figure 2
        """
        data = _load_mtdata('PASC.dat.gz')

        fig = plt.figure()
        ax1 = fig.add_subplot(3, 1, 1)
        ax1.plot(data, color='black')
        ax1.set_xlim(0, len(data))

        spec, freq = mtspec(data, 1.0, 1.5, number_of_tapers=1)

        ax2 = fig.add_subplot(3, 2, 3)
        ax2.set_yscale('log')
        ax2.set_xscale('log')
        ax2.plot(freq, spec, color='black')
        ax2.set_xlim(freq[0], freq[-1])

        spec, freq = mtspec(data, 1.0, 4.5, number_of_tapers=5)

        ax3 = fig.add_subplot(3, 2, 4)
        ax3.set_yscale('log')
        ax3.set_xscale('log')
        ax3.plot(freq, spec, color='black')
        ax3.set_xlim(freq[0], freq[-1])

        spec, freq = sine_psd(data, 1.0)

        ax4 = fig.add_subplot(3, 2, 5)
        ax4.set_yscale('log')
        ax4.set_xscale('log')
        ax4.plot(freq, spec, color='black')
        ax4.set_xlim(freq[0], freq[-1])

        spec, freq = mtspec(data, 1.0, 4.5, number_of_tapers=5, quadratic=True)

        ax5 = fig.add_subplot(3, 2, 6)
        ax5.set_yscale('log')
        ax5.set_xscale('log')
        ax5.plot(freq, spec, color='black')
        ax5.set_xlim(freq[0], freq[-1])

        outfile = os.path.join(self.outpath, 'fig3.pdf')
        fig.savefig(outfile)
        stat = os.stat(outfile)
        self.assertTrue(abs(stat.st_mtime - time.time()) < 3)


def suite():
    return unittest.makeSuite(RecreateFigures, 'test')


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
