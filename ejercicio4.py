print("\n\033[1;31mIngrese tres numeros para sacar el promedio y saber si es par o impar\n")

num1=int(input("\033[1;34mIngrese un numero: "))
num2=int(input("Ingrese otro numero: "))
num3=int(input("Ingrese un tercer numero: "))

suma=int(num1+num2+num3)
promedio=float(suma/3)

if promedio % 2 ==0:
    mensaje="El promedio de los numeros ingresados es par"
else:
    mensaje="El promedio de los numeros ingresados es impar"

print("\n\033[1;35m",mensaje)
print("\033[1;33mEl promedio de los numeros es: ",promedio)