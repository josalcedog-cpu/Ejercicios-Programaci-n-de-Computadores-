# Autor: Daniel Salcedo 
#print  ("Hello World")

#Definición de problemas 


#Solución de Problemas

#Algoritmos

#Encuentre el valor de x en la siguiente ecuación: 

# 2x + 3 = 7
# 2x = 7-3 
# 2x = 4
#(2x)/2 = 4/2 
x = 2

x = print ("Hello")
#print (x) ; no de vuelve nada al ser x una variable nula (print no devuelve datos)
print (type(x))
x1= 7 - 3 
x2 = x1 // 2 # Si opero una división con / me devolverá un float y si lo hago con un // me devolverá un entero 
print(type(x1), x1)
print(type(x2), x2)
print("El valor de x es ", x2)
mensaje = " El valor de la varieble es : "
print(type(mensaje), mensaje)
print(mensaje, x2)

print ("==========================================================================================================")

#Encuentre el valor de x en la siguiente ecuación: 

#AX = B - Z
#Implementar la función input y ezplicar cada parametro efectuado. 
A =int(input("Escriba un numero para la variable A:"))

z1 = int(A)


print (type(A), A)

result = A + 5
print (result)
#====================================================================================================================
print("====================================================================================================================")

print("Actividad : convertir 3 tipos de datos entre cada duno de ells")
print("Str a int:")
x0 = int(input("Escriba el valor para operar: \n "))
print(type(x0),x0)
#
print("str a float:")
x1 = float(input("Escriba el valor para operar: \n "))
print(type(x1),x1)

#
print("int a str:")
x2 = str(input("Escriba el valor para operar: \n "))
print(type(x2),x2)
#
print("int a float:")
x3 = float(input("Escriba el valor para operar: \n "))
print(type(x3),x3)

#====================================================================================================================
print("====================================================================================================================")
#Estructura de control, operaciones logicas
#Booleano, 1,0 
A1= int(input("Digite el dato del if:"))

result =  "A1" + "A1"
if(A1>5): 
    print("Este es el resultado del if verdadero.")
    print(f"La variable A es igual: {A1} ")
else: 
    print("La condicion no se ejecuto:")


print(type(result), result)