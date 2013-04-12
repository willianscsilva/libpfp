class pfp_string:
	def addslashes(self,str):
		return str.replace("'","\\\'").replace("\"","\\\"")

	def explode(self,delimiter,str,limit=0):
		if limit == 0:
			return str.split(delimiter)
		elif type(limit) == int:
			return str.split(delimiter,limit)
		else:
			print "ParameterError: The limit parameter must be a integer" 
