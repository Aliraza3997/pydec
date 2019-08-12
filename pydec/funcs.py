
"""funcs.py: Collection of function related utilities"""

__author__ = "Ali Raza"
__license__ = "MIT"
__version__ = "0.9.0"
__maintainer__ = "Ali Raza"
__email__ = "aliraza3997@gmail.com"
__status__ = "Development"


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


def arg_typecast(*out_args):
    """
    Decorator to typecast input arguments to a function.

    All arguments which match with the provided type are converted to the
    desired type.

    Parameters
    ----------
    *args: tuple(s)
        List of tuples in the form (from_type, to_type) where all arguments with
        type 'from_type' would be typecasted to 'to_type'

    Returns
    -------
    """

    out_args = list(out_args)

    def decorator(func):

        def wrapper(*args, **kwargs):
            args = list(args)

            # Copy args
            for cast_idx, cast in enumerate(out_args):
                from_type, to_type = cast
                from_args_idx = [idx for idx, arg in enumerate(args) if type(arg) == from_type]

                for arg_idx in from_args_idx:
                    args[arg_idx] = to_type(args[arg_idx])

            # Copy key args
            for cast_idx, cast in enumerate(out_args):
                from_type, to_type = cast
                from_args_keys = [arg for arg, value in kwargs.items() if type(value) == from_type]

                for arg_name in from_args_keys:
                    kwargs[arg_name] = to_type(kwargs[arg_name])

            return func(*args, **kwargs)

        return wrapper

    return decorator


def ret_typecast(*out_args):
    """
    Decorator to typecast return of a function.

    All return variables which match with the provided type are converted to the
    desired type.

    Parameters
    ----------
    *args: tuple(s)
        List of tuples in the form (from_type, to_type) where all arguments with
        type 'from_type' would be typecasted to 'to_type'

    Returns
    -------
    """

    out_args = list(out_args)

    def decorator(func):

        def wrapper(*args, **kwargs):
            result = list(func(*args, **kwargs))

            # Copy args
            for cast_idx, cast in enumerate(out_args):
                from_type, to_type = cast
                from_ret_idx = [idx for idx, ret in enumerate(result) if type(ret) == from_type]

                for ret_idx in from_ret_idx:
                    result[ret_idx] = to_type(result[ret_idx])

            return tuple(result)

        return wrapper

    return decorator
