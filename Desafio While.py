print("1)")
numerospares = int(input("Ingrese un primer número: "))
numerospares2= int(input("Ingrese segundo número: "))
if numerospares %2 == 0 and numerospares2 %2 == 0:
    print(numerospares + numerospares2)
else:
    print("los numeros son impares")
print("2)")

contrausuario = input("Usuario, Ingrese contraseña: ")
while contrausuario != "utn750":
    print("Contraseña Incorrecta")
    contrausuario = input("Usuario, Ingrese contraseña: ")
print("Acceso Concedido")
print("3)")
numero09 = int(input("Ingrese un Número: "))
while numero09 <0 or numero09 >9:
    print("numero invalido")
    numero09 = int(input("Ingrese un Número: "))
print("numero valido")
print("4)")
letras = str(input("Ingrese la letra U, o T, o N: "))
while letras !="U" and letras != "T" and letras != "N":
    print("Letra Invalida")
    letras=str(input("Ingrese la letra U, o T, o N: "))
print("Letra Valida")
print("5)")
numero1 = float(input("Ingrese un número: "))
numero2 = float(input("Ingrese segundo número: "))
numero3 = float(input("Ingrese tercer número: "))
numero4 = float(input("Ingrese cuarto número: "))
numero5 = float(input("Ingrese quinto número: ")) 
suma = (numero1+numero2+numero3+numero4+numero5)
print("La suma de sus numeros es",suma)
promedio = suma/5
print("El promedio de sus numeros es)",promedio)