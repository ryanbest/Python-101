import lab04_util

restaurants = lab04_util.read_yelp('yelp.txt')
'''
Function
'''

def print_info(name):
    print name[0]+"(%s)"%(name[5])
    address=name[3].split("+")
    print "\t%s\n\t%s"%(address[0],address[1])
    avg=sum(name[6])/float(len(name[6]))
    print "Average Score: %.2f\n"%(avg)
    
'''
Main
'''
print_info(restaurants[0])
print_info(restaurants[1])