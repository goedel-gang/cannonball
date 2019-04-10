.PHONY:

default: writeup data list .PHONY

data: .PHONY
	(cd graph; ./make_graphs.sh)

writeup: data .PHONY
	(cd writeup; latexmk -pv)

list: data .PHONY
	(cd biglist; latexmk -pv)
