###
##function
###

def center_space_print(width_local,string):
    remain_space_l=(width_local-len(string)-2)/2+(width_local-len(string))%2
    remain_space_r=(width_local-len(string)-2)/2
    return ("*"+" "*remain_space_l+string+" "*remain_space_r+"*"+"\n")
    
def rectange(height,width):
    line1_string="h: %d, w: %d"%(height,width)
    line2_string="area: %d"%(height*width)
    if ((width-2)>=max(len(line1_string),len(line2_string))and(height>=4)):       
        print "*"*width
        print ("*"+" "*(width-2)+"*"+"\n")*((height-2)/2-1)+"%s%s"%(center_space_print(width,line1_string),center_space_print(width,line2_string)),
        print ("*"+" "*(width-2)+"*"+"\n")*((height-2)/2-1+(height-2)%2)+"*"*width       
    else:
        print "*"*width
        print ("*"+" "*(width-2)+"*"+"\n")*(height-2),
        print "*"*width  
        print line1_string+"\n"+line2_string

###
##main
###
height=int(raw_input("Height==> "))
print height
width=int(raw_input("Width==> "))
print width

rectange(height,width)