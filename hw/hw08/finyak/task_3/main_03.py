import formulas

figure = (input('''
1 --> rectangle
2 --> triangle
3 --> circle
Enter the number of figure:                
'''))
if figure == "1":
    length = int(input("Write length: "))
    width = int(input ("Write width: "))
    print (formulas.rectangle(length, width))
elif figure == "2":
    height = int(input("Write height: "))
    mainside = int(input("Write mainside: "))
    print (formulas.triangle(height, mainside))
elif figure == "3":
    radius = int(input("Write radius: "))
    print (formulas.circle(radius))
else: print ("Error")    
