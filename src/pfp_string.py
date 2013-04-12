import htmlentitydefs
import re,cgi,sys
class pfp_string:
	def addslashes(self,str):
		return str.replace("'","\\\'").replace("\"","\\\"")

	def explode(self,delimiter,str,limit=0):
		try:
			if limit == 0:
				return str.split(delimiter)
			elif type(limit) == int:
				return str.split(delimiter,limit)
			else:
				print "Incorrect argument, on method explode(",delimiter,", ",str,", ",limit,"), expected integer" 
		except TypeError, te:
			print "Incorrect argument, on method explode(",delimiter,", ",str,", ",limit,"), expected a character buffer object"
		except AttributeError, ae:
			print "Incorrect argument, on method explode(",delimiter,", ",str,", ",limit,"), expected string"
		except:
			print "Unexpected error:", sys.exc_info()[0]
			raise

	def htmlentities(self,str):
		return cgi.escape(str)

	def html_entity_decode_char(self,m, defs=htmlentitydefs.entitydefs):
		try:
			return defs[m.group(1)]
		except KeyError:
			return m.group(0)

	def html_entity_decode(self,str):
		try:
			pattern = re.compile("&(\w+?);")
			return pattern.sub(self.html_entity_decode_char, str)
		except AttributeError, ae:
			print "Incorrect argument, on method html_entity_decode(",str,"), expected string"
		except TypeError, te:
			print "Incorrect argument, on method html_entity_decode(",str,"), expected string or buffer"
		except:
			print "Unexpected error:", sys.exc_info()[0]
			raise
	
	def implode(self,delimiter,array):
		try:
			return delimiter.join(array)
		except AttributeError, ae:
			print "Incorrect argument, on method implode(",delimiter,", ",array,"), expected string delimiter"
		except TypeError, te:
			print "Incorrect argument, on method implode(",delimiter,", ",array,"), expected list (array)"
		except:
			print "Unexpected error:", sys.exc_info()[0]
			raise

	def lcfirst(self,str):
		try:
			return str.replace(str[0],str[0].lower())
		except AttributeError, ae:
			print "Incorrect argument, on method lcfirst(",str,"), expected string"
		except:
			print "Unexpected error:", sys.exc_info()[0]
			raise

	def ucfirst(self,str):
		try:
			return str.replace(str[0],str[0].upper())
		except AttributeError, ae:
			print "Incorrect argument, on method ucfirst(",str,"), expected string"
		except:
			print "Unexpected error:", sys.exc_info()[0]
			raise
