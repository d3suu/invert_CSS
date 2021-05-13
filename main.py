def invertHexString(hexString):
	standardHex = "0123456789abcdef"
	reversedHex = "fedcba9876543210"
	newString = ['.', '.', '.', '.', '.', '.']
	for i in range(0,6):
		newString[i] = reversedHex[standardHex.find(hexString[i])]
	return ''.join(newString)

def handleLineWithColor(line):
	index = 0;
	newLine = line
	while True:
		b = line.find('#', index)
		if b == -1:
			break
		oldHex = line[b+1:b+7]
		newHex = invertHexString(oldHex)
		newLine = newLine.replace(oldHex, newHex)
		#print("/* GOT COLOR AT " + str(b) + ": " + oldHex + " */")
		#print("/* REVERSED: " + newHex + " */")
		index = b+1
	return newLine

f = open("gitweb.css", "r")
for line in f:
	if '#' in line and ';' in line:
		print(handleLineWithColor(line), end='')
	else:
		print(line, end='')

