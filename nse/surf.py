#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# surf.py


from ._init_surf import _init_cosfield, _init_sinfield
from tfpy.geometry import Surface_BoozerAngle


class IsolatedSurf(Surface_BoozerAngle):


    def __init__(self, r, z, omega, iota: float, reverseToroidalAngle = False, reverseOmegaAngle = True, order: int=1):
        # TODO: Other Conditions for Angles
        assert (not reverseToroidalAngle) and reverseOmegaAngle
        super().__init__(r, z, omega, reverseToroidalAngle, reverseOmegaAngle)
        self.iota = iota
        self.order = order
        self.updateBasis()
        self._init_arr(self.order)
    
    def _init_arr(self, order):
        self.iarr, self.rarr, self.zarr, self.oarr = [self.iota], [self.r], [self.z], [self.omega]
        self.x_psi, self.x_the, self.x_zet = list(), [self.position_theta], [self.position_zeta]
        self.g_pt, self.g_pz = list(), list()
        self.g_tt, self.g_tz, self.g_zz = [self.g_thetatheta], [self.g_thetazeta], [self.g_zetazeta]
        self.Jacobian = list()
        for i in range(order):
            self.iarr.append(0.0)
            self.rarr.append(_init_cosfield(mpol=self.mpol, ntor=self.ntor, nfp=self.nfp))
            self.zarr.append(_init_sinfield(mpol=self.mpol, ntor=self.ntor, nfp=self.nfp))
            self.oarr.append(_init_sinfield(mpol=self.mpol, ntor=self.ntor, nfp=self.nfp))
            self.x_psi.append([
                _init_cosfield(mpol=self.mpol, ntor=self.ntor, nfp=self.nfp),
                _init_sinfield(mpol=self.mpol, ntor=self.ntor, nfp=self.nfp),
                _init_cosfield(mpol=self.mpol, ntor=self.ntor, nfp=self.nfp)
            ])
            self.x_the.append([
                _init_sinfield(mpol=self.mpol, ntor=self.ntor, nfp=self.nfp),
                _init_cosfield(mpol=self.mpol, ntor=self.ntor, nfp=self.nfp),
                _init_cosfield(mpol=self.mpol, ntor=self.ntor, nfp=self.nfp)
            ])
            self.x_zet.append([
                _init_sinfield(mpol=self.mpol, ntor=self.ntor, nfp=self.nfp),
                _init_cosfield(mpol=self.mpol, ntor=self.ntor, nfp=self.nfp),
                _init_cosfield(mpol=self.mpol, ntor=self.ntor, nfp=self.nfp)
            ])
            self.g_pt.append(_init_sinfield(mpol=self.mpol, ntor=self.ntor, nfp=self.nfp))
            self.g_pz.append(_init_sinfield(mpol=self.mpol, ntor=self.ntor, nfp=self.nfp))
            self.g_tt.append(_init_cosfield(mpol=self.mpol, ntor=self.ntor, nfp=self.nfp))
            self.g_tz.append(_init_cosfield(mpol=self.mpol, ntor=self.ntor, nfp=self.nfp))
            self.g_zz.append(_init_cosfield(mpol=self.mpol, ntor=self.ntor, nfp=self.nfp))
            self.Jacobian.append(_init_cosfield(mpol=self.mpol, ntor=self.ntor, nfp=self.nfp))

    def add_order(self, order: int):
        print(f"The order of near-surface expansion will increase from {self.order} to {self.order + order}... ")
        for i in range(order):
            self.iarr.append(0.0)
            self.rarr.append(_init_cosfield(mpol=self.mpol, ntor=self.ntor, nfp=self.nfp))
            self.zarr.append(_init_sinfield(mpol=self.mpol, ntor=self.ntor, nfp=self.nfp))
            self.oarr.append(_init_sinfield(mpol=self.mpol, ntor=self.ntor, nfp=self.nfp))
            self.x_psi.append([
                _init_cosfield(mpol=self.mpol, ntor=self.ntor, nfp=self.nfp),
                _init_sinfield(mpol=self.mpol, ntor=self.ntor, nfp=self.nfp),
                _init_cosfield(mpol=self.mpol, ntor=self.ntor, nfp=self.nfp)
            ])
            self.x_the.append([
                _init_sinfield(mpol=self.mpol, ntor=self.ntor, nfp=self.nfp),
                _init_cosfield(mpol=self.mpol, ntor=self.ntor, nfp=self.nfp),
                _init_cosfield(mpol=self.mpol, ntor=self.ntor, nfp=self.nfp)
            ])
            self.x_zet.append([
                _init_sinfield(mpol=self.mpol, ntor=self.ntor, nfp=self.nfp),
                _init_cosfield(mpol=self.mpol, ntor=self.ntor, nfp=self.nfp),
                _init_cosfield(mpol=self.mpol, ntor=self.ntor, nfp=self.nfp)
            ])
            self.g_pt.append(_init_sinfield(mpol=self.mpol, ntor=self.ntor, nfp=self.nfp))
            self.g_pz.append(_init_sinfield(mpol=self.mpol, ntor=self.ntor, nfp=self.nfp))
            self.g_tt.append(_init_cosfield(mpol=self.mpol, ntor=self.ntor, nfp=self.nfp))
            self.g_tz.append(_init_cosfield(mpol=self.mpol, ntor=self.ntor, nfp=self.nfp))
            self.g_zz.append(_init_cosfield(mpol=self.mpol, ntor=self.ntor, nfp=self.nfp))
            self.Jacobian.append(_init_cosfield(mpol=self.mpol, ntor=self.ntor, nfp=self.nfp))

    def sub_order(self, order: int):
        assert self.order - order >= 0
        print(f"The order of near-surface expansion will be reduced from {self.order} to {self.order - order}... ")
        self.iarr = self.iarr[: self.order-order+1]
        self.rarr = self.rarr[: self.order-order+1]
        self.zarr = self.zarr[: self.order-order+1]
        self.oarr = self.oarr[: self.order-order+1]
        self.x_psi = self.x_psi[: self.order-order]
        self.x_the = self.x_the[: self.order-order+1]
        self.x_zet = self.x_zet[: self.order-order+1]
        self.g_pt = self.g_pt[: self.order-order]
        self.g_pz = self.g_pz[: self.order-order]
        self.g_tt = self.g_tt[: self.order-order+1]
        self.g_tz = self.g_tz[: self.order-order+1]
        self.g_zz = self.g_zz[: self.order-order+1]
        self.Jacobian = self.Jacobian[: self.order-order]
        

if __name__ == "__main__":
    pass
