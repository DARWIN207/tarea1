print("\n\033[1;31mTendra que ingresar dos numeros para poder ver cual es el mayor y el menor")

num1=int(input("\n\033[1;34mIngrese un numero: "))
num2=int(input("Ingrese otro numero: "))
if  num1>num2:
    mensaje = ("El numero mayor es: ", num1, " y el numero menor es: ", num2)
else:
    mensaje = ("El numero mayor es: ", num2, " y el numero menor es: ", num1)

print("\n\033[1;33m",mensaje)