print("\n\033[1;31mTendra que ingresar tres valores numericos")

num1=int(input("\n\033[1;34mIngrese un numero: "))
num2=int(input("Ingrese otro numero: "))
num3=int(input("Ingrese un tercer numero: "))

if num1 > num2 and num1 > num3:
    mensaje="El numero mayor es: ", num1
elif num2 > num1 and num2 > num3:
    mensaje = "El numero mayor es: ", num2
elif num3 > num1 and num3 > num2:
    mensaje = "El numero mayor es: ", num3
else:
    mensaje=("Los numeros son iguales")
print("\n\033[1;32m",num1 , " ", num2 , " " , num3)
print("\033[1;33m",mensaje)