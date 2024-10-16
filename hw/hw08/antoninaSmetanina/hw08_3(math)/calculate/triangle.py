
# Calculate the area of triangle
def area_of_triangle(h, a):
    '''S=0.5*h*a
    h - high
    a - side'''
    s_triangle = 0
    if h > 0 and a > 0:
        s_triangle = 0.5 * h * a
    else:
        print('Triangle does not exist')
    return round(s_triangle, 1)


# print(area_of_triangle(2, 3))

