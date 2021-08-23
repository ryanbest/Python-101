
## Function returns the length of a line 
## starting at (x1,y1) and ending at (x2,y2)
def line_length(x1,y1,x2,y2):
    length = (x1-x2)**2 + (y1-y2)**2
    length = length**(0.5)
    print length
    return length


rotal_distance=line_length(100,100,100,160)+line_length(100,160,80,160)+line_length(80,160,90,120)
print "the total distance the car have traveled is,",rotal_distance
