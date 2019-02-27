rowlist = list()
# a_example
# b_small
# c_medium
# d_big
with  open('d_big.in' , 'r') as f:
	line_one = f.readline().split()
	R = line_one[0]
	C = line_one[1]
	L = line_one[2]
	H = line_one[3]
	
	if (int(H) > int(C)):
		H = C
	
	print('Rows: ' + R)
	print('Columns: ' + C)
	print('Min Ingredient: ' + L)
	print('Max Cells: ' + H)
	print(' ' )
	
	for i in range(int(R)):
		line = f.readline()
		chararray = list(line.strip('\n'))
		
		j = 0
		tcount = 0
		mcount = 0
		for char in chararray:
			if char == 'T':
				tcount += 1
				#print('Tomatos Found on this row: ' +str( tcount) )
			if char == 'M':
				mcount += 1
				#print('Mushroom found on this row: ' + str( mcount))
				
			j += 1
			if j >= int(H):
				break
			
		if ((mcount >= int(L)) and (tcount >= int(L))):
			print('Row ' + str(i) + ' has a valid slice')
			rowlist.append(i)
		#print(chararray)
f.closed

with open('d_big.out', 'w') as out:
	out.write(str(len(rowlist)) + '\n')
	for x in range(len(rowlist)):
		out.write(str(rowlist[x]) + ' 0 ' + str(rowlist[x]) + ' ' + str(int(H) - 1) + '\n')
out.closed