default:
	(cd graph; ./make_graphs.sh)
	(cd writeup; latexmk -pv)
	(cd full_list; latexmk -pv)

full:
	(cd full_list; latexmk -pv)

data:
	(cd graph; ./make_graphs.sh)

writeup:
	(cd writeup; latexmk -pv)
