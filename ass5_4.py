import math

# Constants:
R0 = 10 #kpc # distance from sun to galactic centre in parsecs (approx)

def vel(r, l):
    R = math.sqrt(r**2 + R0**2 + r*R0*math.cos(l)) #kpc
    if R < 5 and R > 0:
        V = 50*R #km/s
    elif R >= 5:
        V = 250 #km/s
    else:
        print "oops.... shouldn't make it to this else"

    return -R0 * V * (r + R0 * math.cos(l)) * math.sin(l)             \
            /(r**2 + R0**2 + 2 * r * R0 * math.cos(l)**(3./2))

def main():
    print vel(10, 0)
    print vel(5, 0)
    print
    print vel(5,math.pi/2)
    print vel(2,math.pi/4)


main()

