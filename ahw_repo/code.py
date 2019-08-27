import numpy as np

def get_neff(s):
    """
    Returns the effective area of a Gaussian PSF

    Parameters
    ----------
    s : float
        sigma of the Gaussian PSF, in pixels

    Returns
    -------
    float
        effective area of the Gaussian PSF, in pixels
    """
    return 4 * np.pi * s * s
