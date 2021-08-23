import math

def line_length(x1,y1,x2,y2):
    distance=int(math.sqrt((x2-x1)**2+(y2-y1)**2))
    print distance
    return distance

rotal_distance=line_length(100,100,100,160)+line_length(100,160,80,160)+line_length(80,160,90,120)

print "the total distance the car have traveled is,",rotal_distance