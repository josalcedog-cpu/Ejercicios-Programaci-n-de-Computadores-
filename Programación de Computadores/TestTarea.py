# Autor: Daniel Salcedo 

print(" Tenemos la siguiente ecuación lineal: AX = B - C \n Encuantre el valor de la variable X según los valores de A,B y C.")

print ("Introduzca los valores enteros para A, B y C: ")
A = int(input ("A:"))
B = int(input ("B:"))
C = int(input ("C:"))

print(" Ahora procedemos a despejar la variable que desconocemos (X)")
print(A,"*X = ",B,"-",C,"\n Luego,")
print("X = ","(",B,"-",C,")/",A, "\n y luego operamos,")
X = int( (B-C)/A)
int(X)
print ("El valor de X es ",X,"\n X =",X)