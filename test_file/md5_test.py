import hashlib

m = hashlib.md5()
m.update(b"Yasin123")
print(m.hexdigest())
m.update(b'Alex123')
print(m.hexdigest())
