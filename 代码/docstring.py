"""This module illustrates how docstrings work.

    In this module, one function f and one class C are defined, each of which has a docstring. C also has one method, which also has a docstring. And here is the docstring for the whole module. 
"""


def f():
    """This function does nothing. """
    pass


class C():
    """This class does nothing. 

        It has no public methods and attributes.

        And no public instance attributes are defined.
    """

    def __init__(self):
        """When initializing this class, no arguments are needed."""
        pass


