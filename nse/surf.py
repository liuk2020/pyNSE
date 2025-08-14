#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# surf.py


from tfpy.geometry import Surface_BoozerAngle


class IsolatedSurf(Surface_BoozerAngle):


    def __init__(self, r, z, omega, iota: float, reverseToroidalAngle = False, reverseOmegaAngle = True):
        super().__init__(r, z, omega, reverseToroidalAngle, reverseOmegaAngle)
        self._iota = iota

    @property
    def iota(self):
        return self._iota


if __name__ == "__main__":
    pass
