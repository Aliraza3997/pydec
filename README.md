
# PyDec -- Collection of Useful decorators for Python
PyDec is a simple set of useful decorators for Python. It allows you to time python functions and more.

## Usage

### 1. Time

Print function execution time.

	from pydec import timer

	@timer.timeit(precision=5)
	def foo(a, b, c, **kwargs):
		...
		
	>>> foo('john', 'doe', debug=True)
	Elapsed time(foo): 0.00238 ms

### 2. Functions
Pass a function arguments by value.

By default all list arguments are passed by value. Type(s) of args can also be
passed to decorator if args of particular type(s) need to be passed by value.

Without args to decorator:

    @funcs.arg_by_value
    def foo(a, b):
        a **= 2
        
        b.append(5)
        
        return a, b
    
    >>> a, b, = np.array([1, 2]), [3, 4]
    >>> foo(a, b)
    >>> print(a, b)
    [1 4] [3, 4]

With args to decorator:

    @funcs.arg_by_value(np.ndarray, list)
    def foo(a, b):
        a **= 2
        
        b.append(5)
        
        return a, b
    
    >>> a, b, = np.array([1, 2]), [3, 4]
    >>> foo(a, b)
    >>> print(a, b)
    [1 2] [3, 4]
    
Typecast input arguments of a function.

Tuples of format (source_type, desired_type) need to be passed to the decorator for casting.

    from pydec import funcs
    import numpy as np
    
    @funcs.arg_typecast((np.ndarray, list), (float, int))
    def foo(a, b, **kwargs):
        print(type(a), type(b))
        a **= 2
		
        return a
        ...
		
	>>> foo(np.array([1, 2]), 10.5)
	<class 'list'> <class 'int'>
	
Typecast return variables from a function.

Tuples of format (source_type, desired_type) need to be passed to the decorator for casting.


    from pydec import funcs
    import numpy as np
    
    @funcs.ret_typecast((np.ndarray, list), (float, int))
	def foo(a, b, **kwargs):
		...
		
	>>> a, b = foo(np.array([1, 2]), 10.5)
    >>> print(type(a), type(b))
	<class 'list'> <class 'int'>
	
### 3. Numpy arrays
Pass numpy.ndarray args by value.

	from pydec import array
    
    arr = np.array([1, 2, 3])
    
	@array.ndarray_copy
	def square(a):
	    a **= 2
		
        return a
        
	>>> print(square(arr))
	[1 4 9]
	>>> print(arr)
	[1 2 3]
	