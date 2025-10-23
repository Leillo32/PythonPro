import random
Bus = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
Dime = int(input("Cual es la longitud de la contraseña"))
Password = ""
for i in range(Dime):
    Password += random.choice(Bus)
print("Tu contraseña generada es"  ,Password)
