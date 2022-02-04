def microscope(a=0, s=1):
    """
    This function returns a painting function that processes a sequence
    of integers, and returns the alternating sum of all integers seen thus
    far (see doctest for an example).

    >>> painting_a = microscope()
    >>> painting_b, x = painting_a(2)
    >>> x                                   # 2
    2
    >>> painting_c, x = painting_b(8)
    >>> x                                   # 2 - 8
    -6
    >>> painting_d, x = painting_c(12)
    >>> x                                   # 2 - 8 + 12
    6
    >>> painting_e, x = painting_d(30)
    >>> x                                   # 2 - 8 + 12 - 30
    -24
    >>> painting_b_again, x = painting_a(100)
    >>> x                                   # 100 [note that we are using painting_a not painting_d here]
    100
    """
    def painting(x):
        return microscope(a=a+s*x, s=-s), a+s*x
    return painting
