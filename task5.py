def triangle_area(side1, side2, side3):
    #https://www.mathsisfun.com/geometry/herons-formula.html
    s = (side1 + side2 + side3) / 2
    r = ((s*(s-side1)*(s-side2)*(s-side3)))** 0.5
    return r
