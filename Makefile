.PHONY:

default: writeup data list .PHONY

data: .PHONY
	(cd graph; ./make_graphs.sh)

writeup: data .PHONY
	(cd writeup; latexmk -pv)

writeup: list .PHONY
	(cd biglist; latexmk -pv)
