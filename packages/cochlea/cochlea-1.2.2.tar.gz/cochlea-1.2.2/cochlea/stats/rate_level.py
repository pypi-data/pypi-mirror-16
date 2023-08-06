# Copyright 2009-2014 Marek Rudnicki

# This file is part of cochlea.

# cochlea is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# cochlea is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with cochlea.  If not, see <http://www.gnu.org/licenses/>.


"""Rate-level charactersitics for inner ear models.

"""
from __future__ import division, print_function, absolute_import

__author__ = "Marek Rudnicki"


import numpy as np
import pandas as pd

import thorns as th
import thorns.waves as wv


def calc_rate_level(
        model,
        dbspls=None,
        cf=1000,
        model_pars=None,
        tone_duration=100e-3,
):
    """Calculate rate-level characteristic of an auditory model.

    Parameters
    ----------
    dbspls : array_like, optional
        An array of sound levels (dB SPL) for which to calculate
        rates.

    """
    if model_pars is None:
        model_pars = {}

    if dbspls is None:
        dbspls = np.arange(-10, 100, 5)

    space = {
        'dbspl': dbspls
    }

    kwargs = {
        'model': model,
        'cf': cf,
        'tone_duration': tone_duration,
        'model_pars': model_pars,
    }

    rates = th.util.map(
        _run_model,
        space,
        kwargs=kwargs,
    )

    return rates



def _run_model(model, dbspl, cf, model_pars, tone_duration):

    onset = 10e-3
    assert tone_duration > onset

    fs = model_pars.setdefault('fs', 100e3)
    model_pars.setdefault('anf_num', (250,250,250))
    model_pars.setdefault('seed', 0)

    sound = wv.ramped_tone(
        fs=fs,
        freq=cf,
        duration=tone_duration,
        pad=0,
        dbspl=dbspl
    )

    anf = model(
        sound=sound,
        cf=cf,
        **model_pars
    )

    rates = {}
    for typ,trains in anf.groupby('type'):
        trimmed = th.trim(trains, onset, None)
        rate = th.firing_rate(trimmed)
        rates[typ] = rate

    return rates
