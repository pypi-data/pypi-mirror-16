#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
3D cell phantom with tilted axis of rotation (FDTD simulation)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The *in silico* data set was created with the 
:abbr:`FDTD (Finite Difference Time Domain)` software `meep`_. The data
are 2D projections of a 3D refractive index phantom that is rotated about
an axis which is tilted by 0.2 rad (11.5 degrees) with respect to the imaging
plane. The example showcases the method :func:`odtbrain.backpropagate_3d_tilted`
which takes into account such a tilted axis of rotation. The data are
downsampled by a factor of two. A total of 220 projections are used for the
reconstruction. Note that the information required for reconstruction
decreases as the tilt angle increases. If the tilt angle is 90 degrees w.r.t.
the imaging plane, then we get a rotating image of a cell (not images of a 
rotating cell) and tomographic reconstruction is impossible. A brief description
of this algorithm is given in [3]_.

.. figure::  ../examples/backprop_from_fdtd_3d_tilted_repo.png
   :align:   center

   3D reconstruction from :abbr:`FDTD (Finite Difference Time Domain)`
   data created by `meep`_ simulations. The first column shows the
   measured phase, visualizing the tilt (compare to other examples). The
   second column shows a reconstruction that does not take into account
   the tilted axis of rotation; the result is a blurry reconstruction.
   The third column shows the improved reconstruction; the known tilted
   axis of rotation is used in the reconstruction process.

Download the :download:`full example <../examples/backprop_from_fdtd_3d_tilted.py>`.
If you are not running the example from the git repository, make sure the
file :download:`example_helper.py <../examples/example_helper.py>` is present
in the current directory.

.. _`meep`: http://ab-initio.mit.edu/wiki/index.php/Meep

This example requires Python3 because the data are lzma-compressed.
"""
from __future__ import division, print_function


def load_tar_lzma_data(afile):
    """
    Load FDTD data from a .tar.lzma file.
    """
    # open lzma file
    with lzma.open(afile, "rb") as l:
        data = l.read()
    # write tar file
    with open(afile[:-5], "wb") as t:
        t.write(data)
    # open tar file
    fields_real = []
    fields_imag = []
    phantom = []
    parms = {}
    
    with tarfile.open(afile[:-5], "r") as t:
        members = t.getmembers()
        members.sort(key=lambda x: x.name)
        
        for m in members:
            n = m.name
            f = t.extractfile(m)
            if n.startswith("fdtd_info"):
                for l in f.readlines():
                    l = l.decode()
                    if l.count("=") == 1:
                        key, val = l.split("=")
                        parms[key.strip()] = float(val.strip())
            elif n.startswith("phantom"):
                phantom.append(np.loadtxt(f))
            elif n.startswith("field"):
                if n.endswith("imag.txt"):
                    fields_imag.append(np.loadtxt(f))
                elif n.endswith("real.txt"):
                    fields_real.append(np.loadtxt(f))

    phantom = np.array(phantom)
    sino = np.array(fields_real)+1j*np.array(fields_imag)
    angles = np.linspace(0, 2*np.pi, sino.shape[0], endpoint=False)
    
    return sino, angles, phantom, parms
    

# All imports are moved to "__main__", because
# sphinx might complain about some imports (e.g. mpl).
if __name__ == "__main__":
    try:
        from example_helper import get_file
    except ImportError:
        print("Please make sure example_helper.py is available.")
        raise
    import lzma  # @UnresolvedImport    # Only Python3
    import tarfile
    import matplotlib.pylab as plt
    import numpy as np
    import os
    from os.path import abspath, dirname, split, join
    import sys
    
    # Add parent directory to beginning of path variable
    DIR = dirname(abspath(__file__))
    sys.path.insert(0, split(DIR)[0])
    
    import odtbrain as odt
    
    try:
        # use jobmanager if available
        import jobmanager as jm
        jm.decorators.decorate_module_ProgressBar(odt, 
                            decorator=jm.decorators.ProgressBarOverrideCount,
                            interval=.1)
    except:
        pass


    lzmafile = get_file("fdtd_3d_sino_A220_R6.500_tiltyz0.2.tar.lzma")
    sino, angles, phantom, cfg = load_tar_lzma_data(lzmafile)

    A = angles.shape[0]
    
    print("Example: Backpropagation from 3d FDTD simulations")
    print("Refractive index of medium:", cfg["nm"])
    print("Measurement position from object center:", cfg["lD"])
    print("Wavelength sampling:", cfg["res"])
    print("Axis tilt in y-z direction:", cfg["tilt_yz"])
    print("Number of projections:", A)
    
    print("Performing normal backpropagation.")
    ## Apply the Rytov approximation
    sinoRytov = odt.sinogram_as_rytov(sino)

    ## Perform naive backpropagation
    f_name_naiv = "f_naiv.npy"
    if not os.path.exists(f_name_naiv):
        f_naiv = odt.backpropagate_3d( uSin=sinoRytov,
                                       angles=angles,
                                       res=cfg["res"],
                                       nm=cfg["nm"],
                                       lD=cfg["lD"]
                                       )
        np.save(f_name_naiv, f_naiv)
    else:
        f_naiv = np.load(f_name_naiv)


    print("Performing tilted backpropagation.")
    ## Determine tilted axis
    tilted_axis = [0, np.cos(cfg["tilt_yz"]), np.sin(cfg["tilt_yz"])]
    
    ## Perform tilted backpropagation
    f_name_tilt = "f_tilt.npy"
    if not os.path.exists(f_name_tilt):
        f_tilt = odt.backpropagate_3d_tilted( uSin=sinoRytov,
                                              angles=angles,
                                              res=cfg["res"],
                                              nm=cfg["nm"],
                                              lD=cfg["lD"],
                                              tilted_axis=tilted_axis,
                                              )
        np.save(f_name_tilt, f_tilt)
    else:
        f_tilt = np.load(f_name_tilt)

    ## compute refractive index n from object function
    n_naiv = odt.odt_to_ri(f_naiv, res=cfg["res"], nm=cfg["nm"])
    n_tilt = odt.odt_to_ri(f_tilt, res=cfg["res"], nm=cfg["nm"])

    sx, sy, sz = n_tilt.shape
    px, py, pz = phantom.shape


    sino_phase = np.angle(sino)    
    
    ## compare phantom and reconstruction in plot
    fig, axes = plt.subplots(2, 3, figsize=(12,7), dpi=300)
    kwri = {"vmin": n_tilt.real.min(), "vmax": n_tilt.real.max()}
    kwph = {"vmin": sino_phase.min(), "vmax": sino_phase.max(), "cmap":plt.cm.coolwarm}  # @UndefinedVariable
    
    
    # Sinorgam
    axes[0,0].set_title("phase projection")    
    phmap=axes[0,0].imshow(sino_phase[int(A/2),:,:], **kwph)
    axes[0,0].set_xlabel("detector x")
    axes[0,0].set_ylabel("detector y")

    axes[1,0].set_title("sinogram slice")    
    axes[1,0].imshow(sino_phase[:,:,int(sino.shape[2]/2)], aspect=sino.shape[1]/sino.shape[0], **kwph)
    axes[1,0].set_xlabel("detector y")
    axes[1,0].set_ylabel("angle [rad]")
    # set y ticks for sinogram
    labels = np.linspace(0, 2*np.pi, len(axes[1,1].get_yticks()))
    labels = [ "{:.2f}".format(i) for i in labels ]
    axes[1,0].set_yticks(np.linspace(0, len(angles), len(labels)))
    axes[1,0].set_yticklabels(labels)

    axes[0,1].set_title("normal (center)")
    rimap = axes[0,1].imshow(n_naiv[int(sx/2)].real, **kwri)
    axes[0,1].set_xlabel("x") 
    axes[0,1].set_ylabel("y")

    axes[1,1].set_title("normal (nucleolus)")
    axes[1,1].imshow(n_naiv[int(sx/2)+2*cfg["res"]].real, **kwri)
    axes[1,1].set_xlabel("x")    
    axes[1,1].set_ylabel("y")

    axes[0,2].set_title("tilt correction (center)")
    axes[0,2].imshow(n_tilt[int(sx/2)].real, **kwri)
    axes[0,2].set_xlabel("x")
    axes[0,2].set_ylabel("y")

    axes[1,2].set_title("tilt correction (nucleolus)")
    axes[1,2].imshow(n_tilt[int(sx/2)+2*cfg["res"]].real, **kwri)
    axes[1,2].set_xlabel("x")
    axes[1,2].set_ylabel("y")

    # color bars
    cbkwargs = {"fraction": 0.045,
                "format":"%.3f"}
    plt.colorbar(phmap, ax=axes[0,0], **cbkwargs)
    plt.colorbar(phmap, ax=axes[1,0], **cbkwargs)
    plt.colorbar(rimap, ax=axes[0,1], **cbkwargs)
    plt.colorbar(rimap, ax=axes[1,1], **cbkwargs)
    plt.colorbar(rimap, ax=axes[0,2], **cbkwargs)
    plt.colorbar(rimap, ax=axes[1,2], **cbkwargs)

    plt.tight_layout()
    
    outname = join(DIR, "backprop_from_fdtd_3d_tilted.png")
    print("Creating output file:", outname)
    plt.savefig(outname)
