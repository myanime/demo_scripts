def NumPad(UnPad,Max):
	PadNum=''
	for x in xrange(len(str(UnPad)),len(str(Max))):
		PadNum+='0'
	PadNum+=str(UnPad)
	return PadNum

def StateTransitions(Sx,Sy,m,n):
	States=''
	Padding=''
	for x in range(0,len(str(m-1))+len(str(n-1))+5):
		Padding+=' '
	if Sx > 0:
		States+='N: ('+NumPad(Sx-1,m-1)+','+NumPad(Sy,n-1)+') '
	else:
		States+='N:'+Padding
	if Sx < m-1:
		States+='S: ('+NumPad(Sx+1,m-1)+','+NumPad(Sy,n-1)+') '
	else:
		States+='S:'+Padding
	if Sy < n-1:
		States+='E: ('+NumPad(Sx,m-1)+','+NumPad(Sy+1,n-1)+') '
	else:
		States+='E:'+Padding
	if Sy > 0:
		States+='W: ('+NumPad(Sx,m-1)+','+NumPad(Sy-1,n-1)+')'
	else:
		States+='W:'+Padding
	return States

def DispTable(m,n):
	NumS = m * n
	Sx = 0
	Sy = 0
	SNum = 1
	for x in xrange(0,NumS):
		States=StateTransitions(Sx,Sy,m,n)
		S='State '+NumPad(SNum,NumS)+': ('+NumPad(Sx,m-1)+','+NumPad(Sy,n-1)+') '
		for St in States:
			S+=St
		print S
		if Sy < n-1:
			Sy+=1
		else:
			Sx+=1
			Sy=0
		SNum+=1

def main():
	m = input('Enter the M(Length) to use: ')
	n = input('Enter the N(Width) to use: ')
	if m < 1 or n < 1:
		print'M or N can not be less than 1.'
		print'Enter a number greater than 0 next time'
		return 1
	else:
		DispTable(m,n)
	return 0

if __name__ == '__main__':
	main()
