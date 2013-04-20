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
		elif argm == "htmlentities":
			print pfp.htmlentities('<b>á</b>')
		elif argm == "html_entity_decode":
			print pfp.html_entity_decode('&lt;b&gt;á&lt;/b&gt;')
		elif argm == "implode":
			array = pfp.explode("-",'20-03-2010')
			print pfp.implode("-",array)
		elif argm == "lcfirst":
			print pfp.lcfirst("HELLO WORLD")
		elif argm == "ucfirst":
			print pfp.ucfirst("hello world")
		elif argm == "levenshtein":
			print pfp.levenshtein("hello","world")
		elif argm == "trim":
			print pfp.trim({" hello ":"hello"})
		elif argm == "ltrim":
			print pfp.ltrim(" hello ")+"world"	
		elif argm == "rtrim":
			print pfp.trim(" hello ")+"world"
		elif argm == "md5":
			print pfp.md5("hello")
		elif argm == "nl2br":
			str = "ola mundo\ncruel"				
			print pfp.nl2br(str)
		elif argm == "number_format":
			print pfp.number_format('1012452.20',2,",","")
		elif argm == "str_replace":
			print pfp.str_replace("o",0,"hello world")
		elif argm == "strip_tags":
			print pfp.strip_tags("<a href=\"#\">click here</a>")
		elif argm == "stripslashes":
			print pfp.stripslashes("Is your name O\'reilly?")
		elif argm == "strlen":
			print pfp.strlen("hello world")
		elif argm == "strpos":
			print pfp.strpos("hello","o")
		elif argm == "strtolower":
			print pfp.strtolower("HELLO WORLD")
		elif argm == "strtoupper":
			print pfp.strtoupper("hello world")
		elif argm == "substr":
			print pfp.substr("hello world",1,7)
			
			
	else:
		program_name = sys.argv[0]
		print "\nIncorrect arguments, see how to use:\n"
		use_list = [program_name+" addslashes",
				program_name+" explode",
				"\n"
			]
		for value in use_list:
			print value
