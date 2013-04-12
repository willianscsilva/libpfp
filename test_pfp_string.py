#!/usr/bin/python
# -*- coding: utf8 -*-
import sys
from src.pfp_string import pfp_string



if __name__ == "__main__":
	pfp = pfp_string()
	if len(sys.argv) > 1:
		argm = sys.argv[1]
		if argm == "addslashes":
			print pfp.addslashes("O'CONNEL")
		elif argm == "explode":
			print pfp.explode("-","2010-20-03")
		elif argm == "html_entities":
			print pfp.html_entities('<b>á</b>')
		elif argm == "html_entity_decode":
			print pfp.html_entity_decode('&lt;b&gt;á&lt;/b&gt;')
		elif argm == "implode":
			array = pfp.explode("-",'20-03-2010')
			print pfp.implode("-",array)
		elif argm == "lcfirst":
			print pfp.lcfirst("HELLO WORLD")
		elif argm == "ucfirst":
			print pfp.ucfirst(1)
	else:
		program_name = sys.argv[0]
		print "\nIncorrect arguments, see how to use:\n"
		use_list = [program_name+" addslashes",
				program_name+" explode",
				"\n"
			]
		for value in use_list:
			print value
