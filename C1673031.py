def doomsday(y):
    
    """
    >>> doomsday(2012)
    3
    >>> doomsday(1899)
    2
    >>> doomsday(1923)
    3
    >>> doomsday(10000)
    -1
    >>> doomsday(1756)
    -1
    >>> type(doomsday(2010))
    <class 'int'>
    """
    if y in range(1800, 1900):
        x = 5
        w = y - 1800
    elif y in range(1900, 2000):
        x = 3
        w= y - 1900
    elif y in range(2000, 2100):
        x = 2
        w = y - 2000
    elif y in range(2100, 2200):
        x = 1
        w = y - 2100
    else:
        return -1              

    a = w // 12
    b = w % 12
    c = b // 4
    d = (a + b + c) % 7
    doomsday = (x + d) % 7
    return doomsday

          