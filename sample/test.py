import hashlib
#           secuer hash algorithm
m = hashlib.sha256()
m.update('1'.encode('utf-8'))
pw = m.digest()
print(pw)

m = hashlib.sha256()
m.update('sksmsdkanrjtehgkftndjqtek'.encode('utf-8'))
pw = m.digest()
print(pw)