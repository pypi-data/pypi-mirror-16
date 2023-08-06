# Licensed under a 3-clause BSD style license - see LICENSE.rst
from __future__ import absolute_import, division, print_function
import os
import numpy as np
from numpy.testing import assert_allclose
from fermipy import castro


def test_castro_test_spectra_sed(tmpdir):
    sedfile = str(tmpdir.join('sed.fits'))
    url = 'https://raw.githubusercontent.com/fermiPy/fermipy-extras/master/data/sed.fits'
    os.system('curl -o %s -OL %s' % (sedfile, url))
    c = castro.CastroData.create_from_sedfile(sedfile)
    test_dict = c.test_spectra()

    assert_allclose(test_dict['PowerLaw']['TS'][0], 26.88, atol=0.01)
    assert_allclose(test_dict['LogParabola']['TS'][0], 27.30, atol=0.01)
    assert_allclose(test_dict['PLExpCutoff']['TS'][0], 28.17, atol=0.01)

    assert_allclose(test_dict['PowerLaw']['Result'], np.array([1.10610705e-16, -3.86502196e+00]))
    assert_allclose(test_dict['LogParabola']['Result'], np.array([4.22089847e-17, -3.71123256e+00, -5.72287142e-02]))
    assert_allclose(test_dict['PLExpCutoff']['Result'], np.array([5.53464102e-13, -2.88974835e+00, 1.19098881e+00]))


def test_castro_test_spectra_castro(tmpdir):
    castrofile = str(tmpdir.join('castro.fits'))
    url = 'https://raw.githubusercontent.com/fermiPy/fermipy-extras/master/data/castro.fits'
    os.system('curl -o %s -OL %s' % (castrofile, url))
    c = castro.CastroData.create_from_fits(castrofile, irow=19)
    test_dict = c.test_spectra()

    assert_allclose(test_dict['PowerLaw']['TS'][0], 0.00, atol=0.01)
    assert_allclose(test_dict['LogParabola']['TS'][0], 0.00, atol=0.01)
    assert_allclose(test_dict['PLExpCutoff']['TS'][0], 2.71, atol=0.01)
