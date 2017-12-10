def read_text(fname):
	with open(fname, "r") as f:
		lines = f.readlines()
	return lines

def read_string(fname):
    with open(fname, "r") as f:
        lines = f.read()
    return lines