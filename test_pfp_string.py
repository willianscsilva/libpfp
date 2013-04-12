import sys
from src.pfp_string import pfp_string



if __name__ == "__main__":
	pfp = pfp_string()
	if len(sys.argv) > 1:
		argm = sys.argv[1]
		if argm == "addslashes":
			print pfp.addslashes("O'CONNEL")
		elif argm == "explode":
			print pfp.explode("-","1982-09-09")
	else:
		program_name = sys.argv[0]
		print "\nIncorrect arguments, see how to use:\n"
		use_list = [program_name+" addslashes",
				program_name+" explode",
				"\n"
			]
		for value in use_list:
			print value
