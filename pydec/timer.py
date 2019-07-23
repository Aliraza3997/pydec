import time


def timeit(precision=2, iters=1):
    """
    Prints the execution time of the decorated function.

    Parameters
    ----------
    precision : int
        Floating point precision of execution time.
    iter : int
        Number of iterations decorated function should be executed for calculating mean time.

    Returns
    -------
    object
        decorator
    """

    if callable(precision):
        def wrapper(*args, **kw):
            ts = time.time()
            result = precision(*args, **kw)
            te = time.time()

            print("Elapsed time({}): {:.2f} ms".format(precision.__name__, (te - ts) * 1000))

            return result

        return wrapper
    else:
        def decorator(func):
            def wrapper(*args, **kw):
                if iters > 1:
                    ts = time.time()
                    for i in range(iters):
                        result = func(*args, **kw)
                    te = time.time()

                    taken = (te - ts) * 1000.0 / iters
                else:
                    ts = time.time()
                    result = func(*args, **kw)
                    te = time.time()
                    taken = (te - ts) * 1000.0

                print("Elapsed time({1}): {2:.{0}f} ms".format(precision, func.__name__, taken))

                return result

            return wrapper

        return decorator
