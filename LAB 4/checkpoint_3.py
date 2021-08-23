import webbrowser

import lab04_util

restaurants = lab04_util.read_yelp('yelp.txt')
'''
Function
'''
def print_review(avg_rating,review_number):
    if avg_rating>=0 and avg_rating<2:
        print "This restaurant is rated bad, based on %d reviews."%(review_number)
    elif avg_rating>=2 and avg_rating<3:
        print "This restaruant is rated average, based on %d reviews."%(review_number)
    elif avg_rating>=3 and avg_rating<4:
        print "This restaurant is rate above average, based on %d reviews."%(review_number)
    elif avg_rating>=4 and avg_rating<5:
        print "This restaurant is rated vert good, based on %d reivews."%(review_number)    

def print_info(rest_list):
    review_number=len(rest_list[6])
    if review_number>=3:
        avg=(sum(rest_list[6])-max(rest_list[6])-min(rest_list[6]))/float(len(rest_list[6])-2)
        print avg
        print_review(avg,review_number)
    else:
        avg=sum(rest_list[6])/review_number
        print_review(avg,review_number)
        ##print "less than 3 reviews"
'''
Main
'''
home_address="56 Republic Dr Bloomfield CT"
idx=int(raw_input("Please provide a restaurant id between 1 and 155==>"))
print idx
if idx>=1 and idx<=150:
    idx-=1
    print_info(restaurants[idx])
    print "What would you like to do next?"
    print "1. Visit the homepage\n2. Show on Google Maps\n3. Show directions to this restaurant"
    idx_1=int(raw_input("Your choice (1-3)? ==>"))
    rest_Web_address=restaurants[idx][4]
    rest_location=restaurants[idx][3].split("+")
    rest_location=rest_location[0]+" "+rest_location[1]
    rest_location_web="http://www.google.com/maps/place/%s"%(rest_location)
    navgiation_to_rest="http://www.google.com/maps/dir/%s/%s)"%(rest_location,home_address)
    if idx_1 == 1:
        webbrowser.open(rest_Web_address)
    elif idx_1 ==2:
        webbrowser.open(rest_location_web)
    elif idx_1 ==3:
        webbrowser.open(navgiation_to_rest)        
else:
    print "Index out of Range, program end"
    




