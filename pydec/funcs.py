import types


def arg_by_value(*out_args):
    """
    Passes arguments to a function by value (by calling their copy() method)

    If no arguments passed to decorator, by default, list type args are passed by value.
    If types are passed as argument to decorator, all args with given types are passed
    by value.

    Note: Each provided type must have a copy() method for this to work e.g list, numpy.ndarray types

    Examples:
        - @args_by_value  # By default list type args are passed by value
        - @args_by_value(np.ndarray, list)  # np.ndarray and list type arguments are passed by value

    Parameters
    ----------
    *args: type(s), optional
        Arbitrary number of types which should be passed by value. If none give, list types are passed
        by value.

    Returns
    -------
    """

    if isinstance(out_args[0], types.FunctionType):
        func = out_args[0]

        def wrapper(*args, **kwargs):
            args = list(args)

            # copy args
            for idx, arg in enumerate(args):
                if type(arg) == list:
                    args[idx] = arg.copy()

            # Copy key args
            for key, value in kwargs.items():
                if type(value) == list:
                    kwargs[key] = value.copy()

            return func(*args, **kwargs)

        return wrapper
    else:
        def decorator(func):
            def wrapper(*args, **kwargs):
                args = list(args)

                # copy args
                for idx, arg in enumerate(args):
                    if type(arg) in out_args:
                        args[idx] = arg.copy()

                # Copy key args
                for key, value in kwargs.items():
                    if type(value) in out_args:
                        kwargs[key] = value.copy()

                return func(*args, **kwargs)

            return wrapper

        return decorator
