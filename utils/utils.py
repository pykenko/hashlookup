def findhash(hashstring, dictio):
	if dictio.get(hashstring):
		print(dictio[hashstring])
	else:
		print("hash not found")