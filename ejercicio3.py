
print("\n\033[1;31mTendra que ingresar tres valores para poder verificar si la summa es multiplo de 7\n")

num1=int(input("\033[1;34mIngrese un numero: "))
num2=int(input("Ingrese otro numero: "))
num3=int(input("Ingrese un tercer numero: "))

suma=int(num1+num2+num3)

if suma%7==0:
    mensaje="La suma \033[1;31mes \033[1;33mmultiplo de 7"
else:
    mensaje="La suma \033[1;31mno es \033[1;33mmultiplo de 7"

print("\n\033[1;33m",mensaje)