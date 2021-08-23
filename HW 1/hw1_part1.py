'''
Functions
'''
def Precentage_Cal(a,b):
	return int(float(b-a)/a*100)

def Print_Compare(a,b,c,d):
	Ice_Precent=Precentage_Cal(a,b)
	alsIce_Precent=Precentage_Cal(c,d)
	print Ice_Precent,"vs",alsIce_Precent

'''
Main
'''
print "#icebucketchallenge vs #alsicebucketchallenge, percentage change"
Print_Compare(200,500,100,300)
Print_Compare(500,2000,300,1500)
Print_Compare(2000,12000,1500,13000)
Print_Compare(12000,24000,13000,25000)
Print_Compare(24000,65000,25000,105000)
Print_Compare(65000,70000,105000,85000)


