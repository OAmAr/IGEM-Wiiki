fname = "bio.txt"
fout = "html2.txt"
def deprec():
	with open(fout,'w') as f:
		for key in sorted(stripped.keys()):
			keystr = "".join(["<h2>","&nbsp;"*2, key, "</h2>","\n"])
			f.write(keystr)
			f.write("<p>\n")
			for val in stripped[key]:
				valstr = "".join(["&nbsp;"*4, val, "<br>", "\n"])
				f.write(valstr)
			f.write("</p>\n")

def getcontents(file):
	with open(file) as f:
		content = f.readlines()
	return content
 
def sortentries(content,numberofentries=3):
	splitOn=numberofentries+1
	rawentries = {}
	for line in range(len(content)):
		name =content[4*(line//4)]
		if line%splitOn == 0:
			rawentries[name] = list()
		else:
			rawentries[name].append(content[line])
	return rawentries

def stripentries(raw):
	#return {key.strip for key in raw: val.strip for val in }
	stripped = {}
	for key in raw:
		stripped[key.strip()] = [line.strip() for line in raw[key]]
	return stripped

def write(clean, fout,format):
	with open(fout,'w') as f:
		for key in sorted(clean):
			pass

def formatted(line, format):
	pass

def main():
	fin = 'bio.txt'
	fout = 'bio.html'
	numentries = 3

	contents = getcontents(fin)
	dictraw = sortentries(contents,3)
	stripped = stripentries(dictraw)
	with open(fout,'w') as f:
		for key in sorted(stripped.keys()):
			keystr = "".join(["<h3.name>",key, "</h3.name>","\n"])
			f.write(keystr)
			f.write("  <p.info>\n")
			for val in stripped[key]:
				valstr = "".join(['    ',val, "<br>", "\n"])
				f.write(valstr)
			f.write("  </p.info>\n")

if __name__ == '__main__':
	main()

