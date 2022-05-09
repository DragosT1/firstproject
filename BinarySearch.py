# Given a file called input.txt, which contains:
# on the first line, an integer number, called X
# on the second line, a list of N sorted integers separated by space, where 0 < N <= 10000
# write a python program that:
# prints the index (position in list) of the first occurrence of X, if X is in the list
# prints -1 if X is not in the list

input = open("input.txt", "r")
lines = input.readlines()

X = lines[0]
listelem = lines[1].split()
minim = listelem[0]
maxim = listelem[len(listelem)]
exists = -1

while maxim>=minim:
	if(X == listelem[maxim]):
		print("Value is found at index: "+ maxim)
		exists = 1
		break
	elif(X < listelem[maxim / 2]):
		maxim = maxim / 2
	else(X > listelem[maxim / 2]): 
		minim = maxim / 2
	
if(exists == -1):
	print(exists)