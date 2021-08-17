"""
A web developer needs to know how to design a web page's size. 
So, given a specific rectangular web page’s area, 
your job by now is to design a rectangular web page, 
whose length L and width W satisfy the following requirements:

The area of the rectangular web page you designed must equal to the given target area.
The width W should not be larger than the length L, which means L >= W.
The difference between length L and width W should be as small as possible.
Return an array [L, W] where L and W are the length and width of the web page you designed in sequence.
"""
def constructRectangle(area):
    if area == 1:
        return [1,1]
    
    mindiff = area
    b = 1
    l = area
    while b < l:
        l = area // b
        if b * l == area and abs(b-l) <= mindiff:
            mindiff = abs(b-l)
            dim = [l,b]
        b += 1
    return dim