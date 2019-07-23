
# PyDec -- Collection of Useful decorators for Python
PyDec is a simple set of useful decorators for Python. It allows you to time python functions and more.

## Usage

Print function execution time.

	from pydec import timer

	@timer.timeit(precision=5)
	def foo(a, b, c, **kwargs):
		...
		
	>>> foo('john', 'doe', debug=True)
	Elapsed time(foo): 0.00238 ms