import numbers
from collections import Sequence

import numpy as np
import scipy.stats as stats


def check_random_state(seed=None):
    """Turn `seed` into a random number generator.

    Parameters
    ----------
    seed : {None, int, array_like[ints], `numpy.random.Generator`,
            `numpy.random.RandomState`, `scipy.stats.qmc.QMCEngine`}, optional

        If `seed` is None fresh, unpredictable entropy will be pulled
        from the OS and `numpy.random.Generator` is used.
        If `seed` is an int or ``array_like[ints]``, a new ``Generator``
        instance is used, seeded with `seed`.
        If `seed` is already a ``Generator``, ``RandomState`` or
        `scipy.stats.qmc.QMCEngine` instance then
        that instance is used.

        `scipy.stats.qmc.QMCEngine` requires SciPy >=1.7. It also means
        that the generator only have the method ``random``.

    Returns
    -------
    seed : {`numpy.random.Generator`, `numpy.random.RandomState`,
            `scipy.stats.qmc.QMCEngine`}

        Random number generator.

    """
    if seed is None or isinstance(seed, (numbers.Integral, np.integer, Sequence)):
        return np.random.default_rng(seed)
    elif isinstance(seed, (np.random.RandomState, np.random.Generator)):
        return seed
    elif hasattr(stats.qmc, "QMCEngine") and isinstance(seed, stats.qmc.QMCEngine):
        return seed
    else:
        raise ValueError(f"{seed:r} cannot be used to seed a"
                         " numpy.random.Generator instance")
