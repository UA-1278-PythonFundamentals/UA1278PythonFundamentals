import area


print("What area you wanna calculate? T - triangle, R - recatangle, C - circle")
option = input()
if option == 'T':
    print("Input side and height")
    a = float(input())
    h = float(input())
    print("The area of triangle is: ", area.tria_area(a, h))

elif option == "R":
    print("Input sides")
    a1 = float(input())
    b = float(input())
    print("The area of triangle is: ", area.rec_area(a1, b))

elif option == "C":
    print("Input radius")
    R = float(input())
    print("The area of triangle is: ", area.cir_area(R))