import hashlib
from .utils import *

dictio = {}
hashes = ["renko", "huang", "tanoto"]

def init():
	for i in hashes:
		dictio[hashlib.md5(i.encode()).hexdigest()] = i
		dictio[hashlib.sha1(i.encode()).hexdigest()] = i
		dictio[hashlib.sha256(i.encode()).hexdigest()] = i
		dictio[hashlib.sha512(i.encode()).hexdigest()] = i

def defaultmd5():
	result = [hashlib.md5(i.encode()).hexdigest() for i in hashes]
	print("to test :")
	for j, i in enumerate(result):
		print(f"hash{j+1}: {i}")

def defaultsha1():
	result = [hashlib.sha1(i.encode()).hexdigest() for i in hashes]
	print("to test :")
	for j, i in enumerate(result):
		print(f"hash{j+1}: {i}")
