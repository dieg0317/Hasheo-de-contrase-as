import bcrypt 

# Contraseña a la que se le aplicará el hash
my_password = b'Sachinfromgeekpython' 

# Generando Salt
salt = bcrypt.gensalt() 

# Hashing de la contraseña
hash_password = bcrypt.hashpw( 
    password=my_password, 
    salt=salt 
) 

print(f"Contraseña actual: {my_password.decode('utf-8')}") 
# Imprimir la contraseña en hash 
print(f"Contraseña en hash: {hash_password.decode('utf-8')}")
