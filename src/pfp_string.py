"""
Author: Willians Costa da Silva
Email: willianscsilva@gmail.com
License: GNU General Public License version 2.0 (GPLv2) - http://www.gnu.org/licenses/gpl-2.0.html
Created: 2013-03-23
Credits & Source:
- The method html_entity_decode() was copied from http://www.php2python.com/
- http://python.org/
Note: Copy, distribute, modify freely, but keep the credits, please.
"""
import htmlentitydefs
import hashlib
import locale
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
				print "Incorrect argument: method explode(",delimiter,", ",str,", ",limit,"), expected integer given ",type(limit)
		except TypeError, te:
			print "Incorrect argument: method explode(",delimiter,", ",str,", ",limit,"), expected a character buffer object given ",type(str)
		except AttributeError, ae:
			print "Incorrect argument: method explode(",delimiter,", ",str,", ",limit,"), expected string given ",type(str)
		except:
			print "Unexpected error:", sys.exc_info()[0]
			raise

	def htmlentities(self,str):
		return cgi.escape(str)

	def __html_entity_decode_char(self,m, defs=htmlentitydefs.entitydefs):
		try:
			return defs[m.group(1)]
		except KeyError:
			return m.group(0)

	def html_entity_decode(self,str):
		try:
			pattern = re.compile("&(\w+?);")
			return pattern.sub(self.__html_entity_decode_char, str)
		except AttributeError, ae:
			print "Incorrect argument: method html_entity_decode(",str,"), expected string given ",type(str)
		except TypeError, te:
			print "Incorrect argument: method html_entity_decode(",str,"), expected string or buffer given ",type(str)
		except:
			print "Unexpected error:", sys.exc_info()[0]
			raise
	
	def implode(self,delimiter,array):
		try:
			return delimiter.join(array)
		except AttributeError, ae:
			print "Incorrect argument: method implode(",delimiter,", ",array,"), expected string delimiter given ",type(delimiter)
		except TypeError, te:
			print "Incorrect argument: method implode(",delimiter,", ",array,"), expected list (array) given ",type(array)
		except:
			print "Unexpected error:", sys.exc_info()[0]
			raise

	def lcfirst(self,str):
		try:
			return str.replace(str[0],str[0].lower())
		except AttributeError, ae:
			print "Incorrect argument: method lcfirst(",str,"), expected string given ",type(str)
		except:
			print "Unexpected error:", sys.exc_info()[0]
			raise

	def ucfirst(self,str):
		try:
			return str.replace(str[0],str[0].upper())
		except AttributeError, ae:
			print "Incorrect argument: method ucfirst(",str,"), expected string given ",type(str)
		except:
			print "Unexpected error:", sys.exc_info()[0]
			raise
			
	"""need to improve performance"""		
	def levenshtein(self,a,b):
		try:
			n, m = len(a), len(b)
			if n > m:
				# Make sure n <= m, to use O(min(n,m)) space
				a,b = b,a
				n,m = m,n

			current = range(n+1)
			for i in range(1,m+1):
				previous, current = current, [i]+[0]*m
				for j in range(1,n+1):
					add, delete = previous[j]+1, current[j-1]+1
					change = previous[j-1]
					if a[j-1] != b[i-1]:
						change = change + 1
					current[j] = min(add, delete, change)            
			return current[n]
		except TypeError, te:
			print "Incorrect argument: method levenshtein(",a,", ",b,"), expected string given ",type(a), " and ",type(b) 
		except KeyError, ke:
			print "Incorrect argument: levenshtein(",a,", ",b,"), expected string given ",type(a), " and ",type(b)
		except:
			print "Unexpected error:", sys.exc_info()[0]
			raise
	
	def trim(self,str):
		try:
			return str.strip()
		except AttributeError, ae:
			print "Incorrect argument: method trim(",str,"), expected string given ",type(str)
		except TypeError, te:
			print "Incorrect argument: method trim(",str,"), expected string given ",type(str)
		except:
			print "Unexpected error:", sys.exc_info()[0]
			raise
	
	def ltrim(self,str):
		try:
			return str.lstrip()
		except AttributeError, ae:
			print "Incorrect argument: method ltrim(",str,"), expected string given ",type(str)
		except TypeError, te:
			print "Incorrect argument: method ltrim(",str,"), expected string given ",type(str)
		except:
			print "Unexpected error:", sys.exc_info()[0]
			raise
	
	def rtrim(self,str):
		try:
			return str.rstrip()
		except AttributeError, ae:
			print "Incorrect argument: method rtrim(",str,"), expected string given ",type(str)
		except TypeError, te:
			print "Incorrect argument: method rtrim(",str,"), expected string given ",type(str)
		except:
			print "Unexpected error:", sys.exc_info()[0]
			raise
	
	def md5(self,str):
		try:
			h = hashlib.md5()
			h.update(str)
			return h.hexdigest()
		except TypeError, te:
			print "Incorrect argument: method md5(",str,"), expected string given ",type(str)
		except:
			print "Unexpected error:", sys.exc_info()[0]
			raise
			
	def nl2br(self,str):
		try:
			return re.sub('[\n\r]','<br />',str)
		except TypeError, te:
			print "Incorrect argument: method nl2br(",str,"), expected string or buffer given ",type(str)
		except:
			print "Unexpected error:", sys.exc_info()[0]
			raise
	
	def number_format(self,num, places=0,sep_dec=".",sep_thous=","):
		try:
			reverse_str = ""
			_str = ""
			num = float(num)	
			
			locale.setlocale(locale.LC_NUMERIC, '')
			if sep_thous != "":
				bool_sep_thous = True
			else:
				bool_sep_thous = False
			num_formated = locale.format("%.*f", (places, num), bool_sep_thous)
			_str = str(num_formated)
			reverse_str = ""
			i=0
			c_thous=0
			for char in _str[::-1]:
				#1.012.452,20			
				if i <= places:				
					if not re.search('[0-9]+',char):
						reverse_str += sep_dec
						c_thous = 1
					else:	
						reverse_str += char
				else:
					if c_thous == 4:
						if not re.search('[0-9]+',char):
							reverse_str += sep_thous
							c_thous = 0
						else:
							reverse_str += char
							c_thous = 1
					else:
						reverse_str += char
				
					c_thous += 1	
				i += 1
			return reverse_str[::-1]
		except TypeError, te:
			print "Incorrect argument: method number_format(",num,"), expected string or a number given ",type(num)
		except:
			print "Unexpected error:", sys.exc_info()[0]
			raise
			