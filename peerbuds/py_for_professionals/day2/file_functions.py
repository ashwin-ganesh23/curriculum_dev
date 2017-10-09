

def read_file(filename):
	fo = open(filename)
	ret = read(fo)
	fo.close()
	return (ret)

def write_file(filename, s):
	fo = open(filename, 'w')
	ret = write(fo, s)
	fo.close()
	return (ret)

def append_file()
