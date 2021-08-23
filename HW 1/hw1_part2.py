
import math
'''
Functions
'''
def remain_return(a,b,c,d,e):
    remove_total=min(a,b,c,d,e)+max(a,b,c,d,e)
    return a+b+c+d+e-remove_total

def spread_return(a,b,c,d,e):
    difference=max(a,b,c,d,e)-min(a,b,c,d,e)
    remain_score_ave=remain_return(a,b,c,d,e)/3
    return float(difference)/remain_score_ave

'''
Main
'''

print "Short program scores 21 32 28 24 29"
print "Free skating scores 24 28 19 23 24"
print "Spread of the short program is",spread_return(21,32,28,24,29)
print "Spread of the free skating is",spread_return(24,28,19,23,24)
print "Total score for the short program is",remain_return(21,32,28,24,29)
print "Total score for the free skating is",remain_return(24,28,19,23,24)
print "The total score for the competitor is",remain_return(24,28,19,23,24)+remain_return(21,32,28,24,29)