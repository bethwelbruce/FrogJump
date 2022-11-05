
def solution(X,Y,D):
    """"
    brute algorithm
    for X=1 to y,x=x+D
    counter increment
    """
    v = (Y -X) // D
    if X+v*D >= Y:
        return v
    else:
        return v+1
    pass
solution(10,85,30)

