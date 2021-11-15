def try_me(a, b):
    """Given two dimensions, a and b, will plot a triangle of that size"""
    import matplotlib.pyplot as plt
    import math
    figure1 = plt.figure(figsize = (10,10))
    plt.plot((0, math.sqrt((a**2)/2)), (0, math.sqrt((a**2)/2)))
    plt.plot((math.sqrt((a**2)/2), math.sqrt((a**2)/2) + math.sqrt((b**2)/2)), (math.sqrt((a**2)/2), math.sqrt((a**2)/2)-math.sqrt((b**2)/2)))
    plt.plot((0,  math.sqrt((a**2)/2) + math.sqrt((b**2)/2)), (0, math.sqrt((a**2)/2)-math.sqrt((b**2)/2)))
    return figure1

