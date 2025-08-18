#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# _init_surf.py


from tfpy.toroidalField import ToroidalField
from tfpy.geometry import Surface_BoozerAngle


def _init_cosfield(mpol: int, ntor: int, nfp: int) -> ToroidalField:
    field = ToroidalField.constantField(0, nfp=nfp, mpol=mpol, ntor=ntor)
    field.reIndex, field.imIndex = True, False
    return field


def _init_sinfield(mpol: int, ntor: int, nfp: int) -> ToroidalField:
    field = ToroidalField.constantField(0, nfp=nfp, mpol=mpol, ntor=ntor)
    field.reIndex, field.imIndex = False, True
    return field


def _init_surf(mpol: int, ntor: int, nfp: int) -> Surface_BoozerAngle:
    return Surface_BoozerAngle(
        r = _init_cosfield(mpol=mpol, ntor=ntor, nfp=nfp),
        z = _init_sinfield(mpol=mpol, ntor=ntor, nfp=nfp),
        omega = _init_sinfield(mpol=mpol, ntor=ntor, nfp=nfp),
        reverseToroidalAngle = False,
        reverseOmegaAngle = True
    )


if __name__ == "__main__": 
    pass
