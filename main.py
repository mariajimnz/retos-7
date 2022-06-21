''' -El valle de aburra afronta altas temperaturas año tras año, Cree una que permita calcular la temperatura media de la tierra partir de recibir 20 datos diarios de temperatura.'''

def temperatura():
    sum=0
    for i in range(20):
        p=int(input("Ingrese la temperatura: "))
        sum=sum+p
    prom=sum/20
    return(int(prom))

print("La temperatura promedio del Valle de Aburrá es: "+str(temperatura()))

'''-Crea una función  que reciba una lista con valores numéricos y devuelva el valor máximo y el mínimo ingresados'''

def maximo(valores):
    mayor = valores[0]

    for i in range(1, len(valores)):
        if valores[i] > mayor:
            mayor = valores[i]

    return mayor

def minimo(valores):
    menor = valores[0]

    for i in range(1, len(valores)):
        if valores[i] < menor:
            menor = valores[i]

    return menor

numeros = [7, 11, 2, 0, 13, 5, -1, -8]

print(maximo(numeros))
print(minimo(numeros))


'''-Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si el nombre de usuario es “admin” y la contraseña es “admin123*”. Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor.'''

usuario = "admin"
contra = "admin123*"
contador = 0
contador1= 0
for i in range(2):
    user = input("Ingrese nombre de usuario: ")
    if user == usuario:
        for i in range(2):
            password = input("Ingresa la contraseña: ")
            if password == contra:
                print("Bienvenido")
                break
            else:
                print("Error")
                contador1 = contador1 +1
    else:
        print("Error de usuario")
        contador = contador + 1

print("Numero de intentos al escribir el usuario",contador)
print("Numero de intentos al escribir la contraseña",contador1)



'''Escriba un programa que pida el ancho y largo de un rectángulo y permita calcular:
-Área
-Perímetro
-Graficar el rectángulo
'''

ancho = int(input("Ingrese base: "))
largo = int(input("Ingrese altura "))


for i in range (1, ancho+1):
    for j in range (1, largo+1):
        print("*", end="")
    print(" ")
