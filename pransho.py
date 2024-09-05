import sys

#print(sys.argv) 
#print(sys.argv[0]) # program name
#print(sys.argv[2]) # first arg
sum  = 0
for arg in sys.argv[1:]:
	
	sum = sum + int(arg)

print(sum)

