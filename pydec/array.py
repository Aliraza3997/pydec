import numpy as np


def ndarray_copy(func):
    """
    A decorator, which passes numpy.ndarray by value in key and key-less arguments

    Checks if any key-less and/or key argument of type np.ndarray. If yes, calls np.copy for
    the argument and then passes to the function.


    Parameters
    ----------
    func: object
        Function to decorate

    Returns
    -------
    object:
        Wrapper function with all key + key-less np.ndarray arguments passed by value (np.copy)
    """

    def wrapper(*args, **kw):
        args = list(args)

        # copy args
        for idx, arg in enumerate(args):
            if type(arg) == np.ndarray:
                args[idx] = arg.copy()

        # Copy key args
        for key, value in kw.items():
            if type(value) == np.ndarray:
                kw[key] = value.copy()

        return func(*args, **kw)

    return wrapper
