
"""contexts.py: Collection of useful Python contexts """

__author__ = "Ali Raza"
__license__ = "MIT"
__version__ = "0.9.0"
__maintainer__ = "Ali Raza"
__email__ = "aliraza3997@gmail.com"
__status__ = "Development"


import pickle


class read_ndarray_pickle:
    """
    Reads pickle file and returns the contents.
    Deletes the numpy array after
    """

    def __init__(self, filename, mode):
        self._filename = filename
        self._mode = mode
        self.arr = None

    def __enter__(self):
        with open(self._filename, self._mode) as f:
            self.arr = pickle.load(f)
            return self.arr

    def __exit__(self, *args):
        self.arr = None
