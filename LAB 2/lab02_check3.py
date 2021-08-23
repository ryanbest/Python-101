bpop_1=100
fpop_1=12

def bpop_cal(bpop,fpop,num):
    bpop_next=max(int((10*bpop)/(1+0.1*bpop) - 0.05*bpop*fpop),0)
    print "bunny population",bpop_next,"in",num,"years"
    return bpop_next
    
def fpop_cal(bpop,fpop,num):
    fpop_next=max(int(0.4 * fpop + 0.02 * fpop * bpop),0)
    print "fox population",fpop_next,"in",num,"years"
    return fpop_next

bpop_1=bpop_cal(bpop_1,fpop_1,1)
fpop_1=fpop_cal(bpop_1,fpop_1,1)
bpop_1=bpop_cal(bpop_1,fpop_1,2)
fpop_1=fpop_cal(bpop_1,fpop_1,2)
bpop_1=bpop_cal(bpop_1,fpop_1,3)
fpop_1=fpop_cal(bpop_1,fpop_1,3)
bpop_1=bpop_cal(bpop_1,fpop_1,4)
fpop_1=fpop_cal(bpop_1,fpop_1,4)
bpop_1=bpop_cal(bpop_1,fpop_1,5)
fpop_1=fpop_cal(bpop_1,fpop_1,5)
bpop_1=bpop_cal(bpop_1,fpop_1,6)
fpop_1=fpop_cal(bpop_1,fpop_1,6)