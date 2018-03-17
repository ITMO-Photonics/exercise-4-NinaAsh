pi = 3.14    
def calculate(R, L):
    surface = 2 * pi * R * (R + L)
    volume = pi * R * R * L 
    return ('surface: ' +  str(surface),
            'Volume: ' +  str(volume))
    
    
R = int(input('Please Enter the radius of a Cylinder: '))
L = int(input('Please Enter the length of a Cylinder: '))

print(calculate(R, L))
