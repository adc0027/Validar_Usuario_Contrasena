user_ = "admin"
password_ = "1234"
print("Bienvenido al sistema de inicio de sesión")
print("Usuario: ")
user = input()
print("Contraseña: ")
password = input()
if user==user_ and password==password_:
    print("Bienvenido al sistema")
else:
    print("Usuario o contraseña incorrectos")
