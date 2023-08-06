# -*- coding: utf-8 -*-
from .ccharts import ccharts
from .tables import D3, D4
import numpy as np

class rbar(ccharts):
    
    def plot(self, ax, data, size):
        assert size >= 2
        assert size <= 10

        R = [] #values
        for xs in data:
            assert len(xs) == size
            R.append(max(xs) - min(xs))

        Rbar = np.mean(R) #center

        lcl = D3[size] * Rbar
        ucl = D4[size] * Rbar
        
        self.elements(ax, R, elements=[lcl, Rbar, ucl])
        return (R, Rbar, lcl, ucl)