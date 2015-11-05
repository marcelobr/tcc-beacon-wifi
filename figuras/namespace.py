
	import hashlib
	import binascii

	# Converte nome de domínio em bytes
	domain_bytes = str.encode('fucapi.br')

	# Gera o hash SHA-1
	hash_sha1 = hashlib.sha1(domain_bytes)

	# Devolve o hash em hexadecimal
	hash_hex = hash_sha1.hexdigest()

	# Converte o hexadecimal em bytes pegando os 10 primeiros
	bytes10 =  bytearray.fromhex(hash_hex)[0:10]

	# Converte os bytes em hexadecimal 
	namespace = binascii.hexlify(bytearray(bytes10))

	print(namespace)



