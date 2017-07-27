import zipfile
zFile = open(sys.argv[1],”r”)
passFile = open(sys.argv[2],”r”)
passwords = passFile.readlines()
for password in passwords:
	try:
		for info in zfile.infolist():
			fname = info.filename
			print "trying..."+str(password)
			data = zfile.read(fname,str(password))
			print “password found:"+str(password))
			break
 	except Exception, e:
 		print e
 			if ('Bad password') in e: pass