
def drive_difference(base10):
    byte_difference=10**9/float(2**30)
    base2=int(base10*byte_difference)
    difference=base10-base2
    print base10,"GB in base 10 is actually,",base2,",GB in base 2,",difference,"GB less than advertised."

base10_1=128    
drive_difference(base10_1)