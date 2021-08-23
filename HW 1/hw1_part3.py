#####
##Function
#####

def volume_soild(width,length,depth):
    return width*length*depth

def water_needed_perlock(volume):
    ships_per_day=35
    water_amount=ships_per_day*volume*365
    return water_amount

#####
##main
#####
volume_per_lock=volume_soild(32,320,10)
water_needed=water_needed_perlock(volume_per_lock)*2
m9_in_days=round(365.0*(9.0/12),-1)
rain_daily_9_m=int(water_needed/m9_in_days)
water_rains=rain_daily_9_m/600000.0

#####
##output
#####

print "The total volume of water needed in Gatun lake:",water_needed,"m^3"
print "In rainy season, daily rain should be at least:",rain_daily_9_m,"m^3"
print "This means, it rains about",water_rains,"millimeters every day during the rainy season:"
