num=int(input("Ingrese un numero entero: "));
if  num > 0:
    mensaje="Es un numero positivo";
elif num == 0:
    mensaje="Es un numero neutro"
else:
    mensaje="El numero es negativo";
print(mensaje);